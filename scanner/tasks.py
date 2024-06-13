from celery import shared_task
from .models import NetworkScan
import nmap
import scapy.all as scapy


@shared_task
def perform_scan(scan_id):
    scan = NetworkScan.objects.get(id=scan_id)
    scan.status = 'RUNNING'
    scan.save()

    try:
        if scan.scan_type == 'ARP':
            results = arp_scan(scan.target_network)
        elif scan.scan_type == 'PING':
            results = ping_sweep(scan.target_network)
        elif scan.scan_type == 'SYN':
            results = syn_scan(scan.target_network)
        elif scan.scan_type == 'OS':
            results = os_detection(scan.target_network)
        else:
            results = 'Unknown scan type'

        scan.scan_results = results
        scan.status = 'COMPLETED'
    except Exception as e:
        scan.status = 'FAILED'
        scan.scan_results = str(e)

    scan.save()


def arp_scan(target_network):
    arp_request = scapy.ARP(pdst=target_network)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    results = []
    for element in answered_list:
        results.append({'ip': element[1].psrc, 'mac': element[1].hwsrc})

    return str(results)


def ping_sweep(target_network):
    nm = nmap.PortScanner()
    nm.scan(hosts=target_network, arguments='-sn')
    hosts = nm.all_hosts()

    results = []
    for host in hosts:
        results.append({'ip': host, 'status': nm[host].state()})

    return str(results)


def syn_scan(target_network):
    nm = nmap.PortScanner()
    nm.scan(hosts=target_network, arguments='-sS')
    hosts = nm.all_hosts()

    results = []
    for host in hosts:
        results.append({
            'ip': host,
            'status': nm[host].state(),
            'open_ports': [port for port in nm[host].all_tcp() if nm[host]['tcp'][port]['state'] == 'open']
        })

    return str(results)


def os_detection(target_network):
    nm = nmap.PortScanner()
    nm.scan(hosts=target_network, arguments='-O')
    hosts = nm.all_hosts()

    results = []
    for host in hosts:
        if 'osclass' in nm[host]:
            os_classes = nm[host]['osclass']
            for os_class in os_classes:
                results.append({
                    'ip': host,
                    'os_type': os_class['type'],
                    'os_vendor': os_class['vendor'],
                    'os_family': os_class['osfamily'],
                    'os_gen': os_class['osgen'],
                    'accuracy': os_class['accuracy']
                })

    return str(results)


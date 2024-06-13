from django.db import models


class NetworkScan(models.Model):
    SCAN_TYPE_CHOICES = [
        ('ARP', 'ARP Scan'),
        ('PING', 'Ping Sweep'),
        ('SYN', 'SYN Scan'),
        ('OS', 'OS Detection'),
    ]

    target_network = models.CharField(max_length=100, help_text="Target network range (e.g., 192.168.1.0/24)")
    scan_type = models.CharField(max_length=10, choices=SCAN_TYPE_CHOICES, default='PING')
    scan_results = models.TextField(help_text="Results of the network scan")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_scan_type_display()} on {self.target_network} at {self.created_at}"


class ScanHistory(models.Model):
    scan = models.ForeignKey(NetworkScan, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('RUNNING', 'Running'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')], default='PENDING')
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Scan {self.scan} - {self.status}"

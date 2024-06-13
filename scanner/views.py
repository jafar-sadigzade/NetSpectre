from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NetworkScan
from .forms import ScanForm
from .tasks import perform_scan


def scan_form(request):
    if request.method == 'POST':
        form = ScanForm(request.POST)
        if form.is_valid():
            scan = form.save()
            perform_scan.delay(scan.id)
            return redirect('scan_results', scan_id=scan.id)
    else:
        form = ScanForm()
    return render(request, 'scanner/scan_form.html', {'form': form})


def scan_results(request, scan_id):
    scan = NetworkScan.objects.get(id=scan_id)
    return render(request, 'scanner/scan_results.html', {'scan': scan})

from django.contrib import admin
from scanner.models import *


@admin.register(NetworkScan)
class NetworkScanAdmin(admin.ModelAdmin):
    pass


@admin.register(ScanHistory)
class ScanHistoryAdmin(admin.ModelAdmin):
    pass
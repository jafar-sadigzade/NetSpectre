from django import forms
from .models import NetworkScan


class ScanForm(forms.ModelForm):
    class Meta:
        model = NetworkScan
        fields = ['target_network', 'scan_type']
        widgets = {
            'target_network': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 192.168.1.0/24'}),
            'scan_type': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ScanForm, self).__init__(*args, **kwargs)
        self.fields['target_network'].label = 'Target Network'
        self.fields['scan_type'].label = 'Scan Type'

from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.scan_form, name='scan_form'),
    path('scan/<int:scan_id>/', views.scan_results, name='scan_results'),
]

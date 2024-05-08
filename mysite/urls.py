"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from invoice import views as invoice_views

urlpatterns = [
    path('submit_invoice/info.html', invoice_views.info_view, name='info'),
    path('', invoice_views.invoice_list_view, name='invoice_list'),  # URL for the invoice list view
    path('submit_invoice/', invoice_views.submit_invoice, name='submit_invoice'),  # URL for submitting an invoice
    path('info.html', invoice_views.info_view, name='info'),
    path('invoice_list.html', invoice_views.invoice_list, name='invoice_list_html'),
    
]
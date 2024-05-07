from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_list_view, name='invoice_list'),
    path('submit_invoice/', views.submit_invoice, name='submit_invoice'),
    path('', views.invoice_list, name='invoice_list'),
    path('info.html', views.info_view, name='info'),
    path('invoice_list/', views.invoice_list_view, name='invoice_list'),
    
]
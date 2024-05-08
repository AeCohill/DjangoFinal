from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_list_view, name='invoice_list'),  # URL for the invoice list view
    path('submit_invoice/', views.submit_invoice, name='submit_invoice'),  # URL for submitting an invoice
    path('info.html', views.info_view, name='info'),
    path('invoice_list.html', views.invoice_list, name='invoice_list_html'),
    path('submit_invoice/info.html', views.info_view, name='info'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('info.html', views.info_view, name='info'),
    path('', views.invoice_list_view, name='invoice_list'),
    path('submit_invoice/', views.submit_invoice, name='submit_invoice'),    path('info/', views.info_view, name='info'),  # URL for the info view
    path('invoice_list.html', views.invoice_list_view, name='invoice_list_html'),  # URL for the invoice list view
    path('submit_invoice/info/', views.info_view, name='info'),  # URL for the info view within the submit_invoice path
    path('submit_invoice/invoice_list/', views.info_view, name='info'),  # URL for the info view within the submit_invoice path
]

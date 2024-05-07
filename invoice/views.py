from django.shortcuts import render, redirect
from .forms import InvoiceForm
from django.db import models
from .models import Invoice

def submit_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            # Process the form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            address = form.cleaned_data['address']
            service = form.cleaned_data['service']
            
            # After processing, redirect the user to the invoice list page
            return redirect('invoice_list')  # Assuming 'invoice_list' is the name of your URL pattern for invoice list
    else:
        form = InvoiceForm()

    return render(request, 'invoice_list.html', {'form': form})
def invoice_list(request):
    return render(request, 'invoice/invoice_list.html', {})

def info_view(request):
    return render(request, 'invoice/info.html')

def invoice_list_view(request):
    # Logic to retrieve invoices from the database
    invoices = Invoice.objects.all()  # Fetch invoices from the database or any other source
    return render(request, 'invoice_list.html', {'invoices': invoices})

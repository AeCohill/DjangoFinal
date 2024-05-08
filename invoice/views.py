from django.shortcuts import render, redirect
from .forms import InvoiceForm
from django.db import models
from .models import Invoice
from django.shortcuts import render, redirect
from .forms import InvoiceForm
from .models import Invoice

def submit_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            
            new_invoice = Invoice(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                address=form.cleaned_data['address'],
                service=form.cleaned_data['service']
            )
            
            new_invoice.save()
           
            return redirect('invoice_list')  
    else:
        form = InvoiceForm()

    return render(request, 'invoice_list.html', {'form': form})

def invoice_list(request):
    invoices = Invoice.objects.all()

    return render(request, 'invoice_list.html', {'invoices': invoices})
def info_view(request):
    return render(request, 'invoice/info.html')

def invoice_list_view(request):
    invoices = Invoice.objects.all()  
    return render(request, 'invoice_list.html', {'invoices': invoices})

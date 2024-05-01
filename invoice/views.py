from django.shortcuts import render

def invoice_list(request):
    return render(request, 'invoice/invoice_list.html', {})

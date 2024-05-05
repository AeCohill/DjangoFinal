from django.shortcuts import render

def invoice_list(request):
    return render(request, 'invoice/invoice_list.html', {})

def info_view(request):
    return render(request, 'invoice/info.html')

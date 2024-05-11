from django import forms

class InvoiceForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, required=True)
    last_name = forms.CharField(label='Last Name', max_length=100, required=True)
    address = forms.CharField(label='Address', max_length=200, required=True)
    service = forms.CharField(label='Service', max_length=100, required=True)
    price = forms.CharField(label='Price', max_length=100, required=True)
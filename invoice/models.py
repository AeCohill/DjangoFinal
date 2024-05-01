from django.conf import settings
from django.db import models
from django.utils import timezone
import random

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)

class Service(models.Model):
    description = models.CharField(max_length=200)
    trees = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    hours = models.DecimalField(max_digits=5, decimal_places=2)

    def calc_cost(self):
        return self.rate * self.hours + (self.trees * 300)

class Invoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def gen_invoice_id(self):
        self.invoice_id = random.randint(1, 50000)

    def create_invoice(self, name, address, phone, details, trees, rate, hours):
        invoice_id = self.gen_invoice_id()
        print(f"Invoice ID: {invoice_id}")

        customer = Customer.objects.create(name=name, address=address, phone=phone)
        service = Service.objects.create(description=details, trees=trees, rate=rate, hours=hours)
        cost = service.calc_cost()
        
        invoice = Invoice.objects.create(invoice_id=invoice_id, customer=customer, service=service, cost=cost)
        print(f"Success! Invoice created: {invoice}")

    def get_invoice(self, invoice_id):
        try:
            invoice = Invoice.objects.get(invoice_id=invoice_id)
            print(f"Invoice ID: {invoice.invoice_id}")
            print(f"Customer name: {invoice.customer.name}")
            print(f"Customer address: {invoice.customer.address}")
            print(f"Customer phone number: {invoice.customer.phone}")
            print(f"Service details/description: {invoice.service.description}")
            print(f"Number of trees: {invoice.service.trees}")
            print(f"Rate per hour: {invoice.service.rate}")
            print(f"Number of hours: {invoice.service.hours}")
            print(f"Total cost: {invoice.cost}")
        except Invoice.DoesNotExist:
            print("Invoice not found.")

    def print_all_invoices(self):
        """
        Prints all invoices currently stored.
        """
        invoices = Invoice.objects.all()
        if not invoices:
            print("No invoices found.")
            return

        for invoice in invoices:
            print(f"Invoice ID: {invoice.invoice_id}")
            print(f"Customer name: {invoice.customer.name}")
            print(f"Customer address: {invoice.customer.address}")
            print(f"Customer phone number: {invoice.customer.phone}")
            print(f"Service details/description: {invoice.service.description}")
            print(f"Number of trees: {invoice.service.trees}")
            print(f"Rate per hour: {invoice.service.rate}")
            print(f"Number of hours: {invoice.service.hours}")
            print(f"Total cost: {invoice.cost}")
            print("-" * 50)


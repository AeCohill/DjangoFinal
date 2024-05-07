from django.db import models

class Invoice(models.Model):
    # Define a new primary key field
    invoice_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    service = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Invoice #{self.invoice_id}: {self.first_name} {self.last_name}"

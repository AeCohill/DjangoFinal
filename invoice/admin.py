from django.contrib import admin
from .models import Customer
from .models import Service
from .models import Invoice


admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(Invoice)

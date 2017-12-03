from contact.models import Order
from contact.models import Contact
from contact.models import Retailer
from contact.models import Item
from django.contrib import admin

# Register your models here.
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(Retailer)
admin.site.register(Item)
admin.site.register(Comment)
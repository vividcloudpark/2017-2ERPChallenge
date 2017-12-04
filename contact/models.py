from django.db import models
import datetime


class Item (models.Model):
    item_id = models.CharField(primary_key=True, max_length=10)
    item_name = models.CharField(max_length=50)
    item_price = models.CharField(max_length=10)
    item_origin = models.CharField(max_length=2)

    def __str__(self):
        return self.item_name

    def dic(self):
        fields = ['item_id', 'item_name', 'item_price', 'item_origin']
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result


class Retailer (models.Model):
    company_name = models.CharField(primary_key=True, max_length=20)
    company_address = models.TextField(max_length=200)
    company_zipcode = models.CharField(max_length=5)
    company_country = models.CharField(max_length=2)

    def __str__(self):
        return "[" + self.company_country + "] " + self.company_name

    def dic(self):
        fields = ['company_name', 'company_address', 'company_zipcode', 'company_country']
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result

class Order (models.Model):
    order_id = models.CharField(max_length=6, primary_key=True, unique=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    shipping_address = models.TextField(max_length=200)
    shipping_zipcode = models.CharField(max_length=6)
    shipping_country = models.CharField(max_length=2)
    def __str__(self):
        return "[" + self.shipping_country + "] " + self.order_id

    def dic(self):
        fields = ['Order_id', 'item_id', 'shipping_address', 'shipping_country']
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result

class Contact (models.Model):
    contact_company_name = models.CharField(max_length=20)
    customer_email = models.CharField(max_length=100)
    order_number = models.CharField(max_length=6)
    contact_country = models.CharField(max_length=2)
    contact_question = models.TextField(max_length=200)
    contact_time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return "Question from  " + self.contact_company_name

    def dic(self):
        fields = ['contact_company_name', 'customer_email', 'order_number', 'contact_question', 'contact_time']
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result



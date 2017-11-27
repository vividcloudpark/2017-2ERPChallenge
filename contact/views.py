from django.shortcuts import render
from django.shortcuts import Http404
from .models import Contact
from .models import Retailer
import json


def index(request):
    return render(request, 'base.html')

def contact(request):
    return render(request, 'contact.html')

def work(request):
    return render(request, 'work.html')

def contact_success(request):
    all_contact = None
    if request.method == 'POST':
        contact = Contact(
            contact_company_name = request.POST['Companyname'],
            customer_email = request.POST['email'],
            order_number = request.POST['order_number'],
            contact_country = request.POST['contact_country'],
            contact_question = request.POST['contact_question']
        )
        contact.save()
        all_contact = Contact.objects.all()
    return render(request, 'contact_success.html')


def work_success(request):
    tag = request.POST['Companyname']
    try:
        retailertag = Retailer.objects.get(pk=tag)
        data = retailertag.dic()
        name = data['company_name']
        address = data['company_address']
        zipcode = data['company_zipcode']
        country = data['company_country']

    except:
        data = "Sorry! DBFINDER couldn't find about    " + tag + " !"

    print(data)
    return render(request, 'work_success.html', {'name' : name , 'address' : address,
                                                 'zipcode' : zipcode,'country' : country, 'tag': tag})
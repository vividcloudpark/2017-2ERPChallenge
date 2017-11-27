from django.shortcuts import render
from django.shortcuts import Http404
from .models import Contact
from .models import Retailer
from .models import Item
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


def work_find_by_company(request):
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
    return render(request, 'work_find_by_company.html', {'name' : name , 'address' : address,
                                                 'zipcode' : zipcode,'country' : country, 'tag': tag})

def work_find_by_itemid(request):
    tag = request.POST['itemid']
    try:
        itemtag = Item.objects.get(pk=tag)
        data = itemtag.dic()
        name = data['item_name']
        price = data['item_price']
        origin = data['item_origin']

    except:
        return Http404("Sorry! DBFINDER couldn't find about    " + tag + " !")

    print(data)
    return render(request, 'work_find_by_itemid.html', {'name' : name , 'price' : price,
                                                 'origin' : origin, 'tag': tag})


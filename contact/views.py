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
    contact_results = Contact.objects.filter(contact_company_name = tag).exists()
    retailer_results = Retailer.objects.filter(pk=tag).exists()

    if retailer_results or contact_results != False:
        if retailer_results != False and contact_results == False:
            retailertag = Retailer.objects.get(pk=tag)
            data = retailertag.dic()
            return render(request, 'work_find_by_company.html', {'tag': tag, 'data': data})

        elif retailer_results == False and contact_results != False:
            contact_data = []
            for i in Contact.objects.filter(contact_company_name=tag):
                contact_tag = i
                temp_data = contact_tag.dic()
                contact_data.append(temp_data)
            return render(request, 'work_find_by_company.html', {'tag': tag, 'contact': contact_data[0]})

        else:
            retailertag = Retailer.objects.get(pk=tag)
            data = retailertag.dic()
            contact_data = []
            for i in Contact.objects.filter(contact_company_name=tag):
                contact_tag = i
                temp_data = contact_tag.dic()
                contact_data.append(temp_data)
            return render(request, 'work_find_by_company.html', {'tag': tag, 'data': data, 'contact': contact_data[0]})


    else:
        raise Http404("Sorry! DBFINDER couldn't find about    " + tag + " !")


def work_find_by_itemid(request):
    tag = request.POST['itemid']
    try:
        itemtag = Item.objects.get(pk=tag)
        data = itemtag.dic()

    except:
        return Http404("Sorry! DBFINDER couldn't find about    " + tag + " !")

    print(data)
    return render(request, 'work_find_by_itemid.html', {'tag': tag, 'data' : data})


from django.http import HttpResponse
from django.shortcuts import render

def get_index(request):
    # return render(request, 'catalog/index.html')
    return HttpResponse("Index page")

def get_contacts(request):
    # return render(request, 'catalog/contacts.html')
    return HttpResponse("Contacts page")
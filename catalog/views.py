from django.http import HttpResponse
from django.shortcuts import render


def get_index(request):
    return render(request, 'catalog/index.html')


def get_contacts(request):
    return render(request, 'catalog/contacts.html')

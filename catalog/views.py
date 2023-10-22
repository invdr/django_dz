from django.http import HttpResponse
from django.shortcuts import render


def get_index(request):
    return render(request, 'catalog/index.html')


def get_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Новое сообщение от {name}({phone}): {message}')
    return render(request, 'catalog/contacts.html')

from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


def get_index(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Каталог товаров - MyStore',
        'section_name': 'Каталог',
    }

    return render(request, 'catalog/index.html', context)


def get_contacts(request):
    context = {
        'title': 'Контакты',
        'section_name': 'Контакты',
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Новое сообщение от {name}({phone}): {message}')
    return render(request, 'catalog/contacts.html', context)


def get_product_info(request, product_pk):
    products_list = Product.objects.all()
    context = {
        'product_info': products_list.get(pk=product_pk),
        'section_name': 'Информация о продукте',
    }

    return render(request, 'catalog/product_details.html', context)

from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    paginate_by = 4

    extra_context = {
        'title': 'Каталог товаров - MyStore',
        'section_name': 'Каталог',
    }


class ProductDetailView(DetailView):
    model = Product

    extra_context = {
        'section_name': 'Информация о продукте',
    }


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

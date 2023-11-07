from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import get_index, get_contacts, get_product_info

app_name = CatalogConfig.name


urlpatterns = [
    path('', get_index, name='index'),
    path('contacts/', get_contacts, name='contacts'),
    path('product_details/<int:product_pk>/', get_product_info, name='product')

]

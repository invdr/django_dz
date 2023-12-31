from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import get_contacts, ProductListView, ProductDetailView

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', get_contacts, name='contacts'),
    path('product_details/<int:pk>/', ProductDetailView.as_view(), name='product')

]

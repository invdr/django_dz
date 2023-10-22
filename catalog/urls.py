from django.urls import path

from catalog.views import get_index, get_contacts

urlpatterns = [
    path('', get_index),
    path('contacts/', get_contacts)
]

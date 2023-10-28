import json

from django.core.management import BaseCommand, call_command

from catalog.models import Category, Product


class Command(BaseCommand):

    @classmethod
    def delete_data(cls, model):
        model.objects.all().delete()
        model.objects.all().delete()

    def handle(self, *args, **options):
        for model in (Category, Product):
            self.delete_data(model)

        call_command('loaddata', 'catalog_data.json')

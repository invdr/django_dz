# Generated by Django 4.2.6 on 2023-10-28 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_category_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['pk'], 'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
    ]

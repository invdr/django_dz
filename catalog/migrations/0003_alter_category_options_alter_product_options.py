# Generated by Django 4.2.6 on 2023-10-28 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_category_id_alter_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('pk',), 'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('pk',), 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]
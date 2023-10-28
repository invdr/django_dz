from django.db import models

NULLABLE = {"null": True, "blank": True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ('pk',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="product_images/", verbose_name="Превью продукта", **NULLABLE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.IntegerField(default=0, verbose_name="Цена")
    created_at = models.DateTimeField(verbose_name="Дата создания")
    last_change = models.DateTimeField(verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.name} ({self.category_id.name})"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ('pk', )

from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=200, null=False, blank=False, verbose_name='Категория')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    changed_at = models.DateField(auto_now=True, verbose_name='Дата обновления')


class Product(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False, verbose_name='Продукт')
    price = models.DecimalField(null=False, blank=False, max_digits=12, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(
        verbose_name='Категория',
        to='webapp.Category',
        null=True,
        blank=True,
        related_name='categories',
        on_delete=models.RESTRICT
    )
    image = models.CharField(max_length=300, null=True, blank=True, verbose_name="Описание")
    description = models.TextField(null=False, blank=False, verbose_name="Описание")
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_updated = models.DateField(auto_now=True, null=True, blank=True, verbose_name='Дата обновления')

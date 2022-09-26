from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=50, null=False, blank=False, verbose_name='Категория')
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    changed_at = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата обновления')


class Product(models.Model):
    no_category = (None, '')

    title = models.CharField(max_length=65, null=False, blank=False, verbose_name='Продукт')
    price = models.DecimalField(null=False, blank=False, max_digits=12, decimal_places=2, verbose_name='Цена')
    image = models.CharField(max_length=300, null=True, blank=True, verbose_name="Изображние")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    category = models.ForeignKey(
        verbose_name='Категория',
        to='webapp.Category',
        null=True,
        blank=True,
        related_name='products',
        on_delete=models.RESTRICT
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='Дата создания')
    changed_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True,
                                      verbose_name='Дата обновления')

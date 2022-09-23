from django.urls import path

from webapp.views.base import home_view
from webapp.views.products import products_view

urlpatterns = [
    path('/', home_view, name='home'),
    path('/products', products_view, name='show_products')
]

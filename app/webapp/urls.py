from django.urls import path

from webapp.views.base import home_view
from webapp.views.categories import categories_view, add_category_view, delete_category_view, edit_category_view
from webapp.views.products import products_view, product_view, add_view, edit_view, delete_view

urlpatterns = [
    path('', home_view, name='home'),
    path('products/', products_view, name='show_products'),
    path('products/add/', add_view, name='add_product'),
    path('products/<pk>/', product_view, name='show_product'),
    path('products/edit/<pk>', edit_view, name='edit_product'),
    path('products/delete/<pk>', delete_view, name='delete_product'),
    path('categories/', categories_view, name='show_categories'),
    path('categories/add/', add_category_view, name='add_category'),
    path('categories/delete/<pk>', delete_category_view, name='delete_category'),
    path('categories/edit/<pk>', edit_category_view, name='edit_category')

]

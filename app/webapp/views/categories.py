from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models import Product, Category


def add_category_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'add_category.html')
    category = Category.objects.create(
        category=request.POST.get('category'),
        description=request.POST.get('description'),
    )
    category.save()
    url = reverse('show_categories')
    return HttpResponseRedirect(url)


def categories_view(request: WSGIRequest):
    categories = Category.objects.all()
    return render(request, 'categories.html', context={'categories': categories})


def edit_category_view(request: WSGIRequest, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'GET':
        return render(request, 'add_category.html', context={'category': category})
    category.category = request.POST.get('category')
    category.description = request.POST.get('description')
    category.save()
    return redirect('show_categories')


def delete_category_view(request: WSGIRequest, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('show_categories')

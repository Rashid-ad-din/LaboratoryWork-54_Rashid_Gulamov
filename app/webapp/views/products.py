from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models import Product, Category


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        categories = Category.objects.all()
        print(categories)
        return render(request, 'add_product.html', context={'categories': categories})
    product = Product.objects.create(
        title=request.POST.get('title'),
        price=request.POST.get('price'),
        image=request.POST.get('image'),
        description=request.POST.get('description'),
        category=Category.objects.get(pk=request.POST.get('category'))
    )
    product.save()
    url = reverse('show_product', kwargs={'pk': product.pk})
    return HttpResponseRedirect(url)


def products_view(request: WSGIRequest):
    products = Product.objects.all()
    return render(request, 'products.html', context={'products': products})


def product_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product})


def edit_view(request: WSGIRequest, pk):
    categories = Category.objects.all()
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'add_product.html',
                      context={
                          'product': product,
                          'categories': categories
                      })
    product.title = request.POST.get('title')
    product.price = request.POST.get('price')
    product.image = request.POST.get('image')
    product.description = request.POST.get('description')
    product.category = Category.objects.get(pk=request.POST.get('category'))
    product.save()
    return redirect('show_product', pk=product.pk)


def delete_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('show_products')

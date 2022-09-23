from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def products_view(request: WSGIRequest):
    return render(request, 'products.html')

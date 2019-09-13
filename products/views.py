from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request,
                  "index.html",
                  {'products': products})  # can't be {products} like in JavaScript


def new(request):
    return HttpResponse('New Page')


from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Product, Category
from django.views.generic import ListView
from .cart import *
from .cart import Cart
from .forms import CartAddProductForm


def index(request):
    """View function for home page of site."""
    # Fetch all categories
    all_category = Category.objects.all()

    context = {
        'product_category': all_category,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)


class ProductList(ListView):
    model = Product


def product_list(request):
    """View show all the products in the store"""
    product = Product.objects.all()
    context = {
        'products': product,
    }

    return render(request, 'cart/product_list.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    context = {
       'product': product,
    }
    return render(request, 'cart/product_detail.html', context)


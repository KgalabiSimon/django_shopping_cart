from django.shortcuts import render

# Create your views here.
from .models import Product, Category
from django.views.generic import ListView


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


def product_cart(request):
    """View show product for product cart"""
    product = Product.objects.all()
    context = {
        'product': product,
    }

    return render(request, 'product_cart.html', context)

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
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'cart_product_form': cart_product_form,

    }
    return render(request, 'cart/product_detail.html', context)


def add_product_cart_form(request, product_id):
    """form for adding a product to their cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart-detail')


def cart_detail(request):
    """View for displaying the cart"""
    cart = Cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'cart/detail.html', context)


def cart_remove(request, product_id):
    """view for removing product in the cart"""

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart-detail')


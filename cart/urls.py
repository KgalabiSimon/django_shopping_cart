from django.contrib import admin
from django.urls import path
from . import views
from cart.views import ProductList
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='products-list'),
    path('product/<int:product_id>', views.product_detail, name='product-detail'),
    path('add/<int:product_id>', views.add_product_cart_form, name='product-add'),
    path('cart/', views.cart_detail, name='cart-detail'),
    path('remove/<int:product_id>',views.cart_remove, name='cart_remove'),



]
from django.contrib import admin
from django.urls import path
from . import views
from cart.views import ProductList
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='products-list'),
    path('product/<int:product_id>', views.product_detail, name = 'product-detail')


]
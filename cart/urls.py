from django.contrib import admin
from django.urls import path
from . import views
from cart.views import ProductList
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', ProductList.as_view(), name='product-list' )
]
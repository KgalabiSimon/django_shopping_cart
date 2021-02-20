from django.db import models
from django.urls import reverse
import django_filters


class Category(models.Model):
    """Model representing a product category (e.g Cellphones, Computers, Clothes, """
    name = models.CharField(max_length=30)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Product(models.Model):
    """Model representing a Product"""
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, )
    items_bought = models.IntegerField()
    image = models.ImageField(upload_to='cart/static/cart')

    def items_bought(self):
        """adds and appends the number of products bought """
        self.items_bought += 1

    def get_absolute_url(self):
        """Returns the url to access a particular product instance."""
        return reverse('product-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name


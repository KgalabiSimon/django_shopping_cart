from django.conf import settings
from .models import Product

class Cart(object):

    def __init__(self, request):
        """Initialise the cart"""
        self.session = request.session
        self.cart = self.session.get(settings.CART_SESSION_ID)
        if not self.cart:
            # save an empty cart in the session
            self.cart = self.session[settings.CART_SESSION_ID] = {}
            self.cart = self.cart

    def add(self, product, quantity=1, update_quantity=False):
        """Add a product to the cart or update its quantity"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                    'quantity': 0,
                    'price': str(product.price),

                }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as modified to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """Remove a product from the cart"""
        self.product_id = str(product.id)
        if self.product_id in self.cart:
            del self.cart[self.product_id]
            self.save()

    def __iter__(self):
        """Iterate overt the items in the cart and get the products"""
        product_ids = self.cart.keys()
        # get the product and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Count all the items in the cart"""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """calculate the total price"""
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from the session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

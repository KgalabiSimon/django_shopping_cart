# django_shopping_cart
django-cart is a very simple application that just let you add and remove items from a session based cart. django-cart uses the power of the Django content type framework to enable you to have your own Product model and associate with the cart without having to change anything

# Demo Link
https://kgalabiecommerce.herokuapp.com/cart/

# Quick Start

* To get this project up and running locally on your computer:


  * 1.Set up the Python development environment. We recommend using a Python virtual environment.
  * 2.Assuming you have Python setup, run the following commands (if you're on Windows you may use py or py -3 instead of python3 to start Python):
      * pip3 install -r requirements.txt
      * python3 manage.py makemigrations
      * python3 manage.py migrate
      * python3 manage.py createsuperuser # Create a superuser
      * python3 manage.py runserver
      * Open a browser to http://127.0.0.1:8000/admin/ to open the admin site
      * Create a few test objects of each type.
      * Open tab to http://127.0.0.1:8000 to see the main site, with your new objects.



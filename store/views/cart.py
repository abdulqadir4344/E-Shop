from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer

from django.views import View
from store.models.product import Product
from django.views.decorators.csrf import csrf_exempt



#For Login
class Cart(View):
    @csrf_exempt
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products': products})

    
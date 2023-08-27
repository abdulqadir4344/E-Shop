from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer

from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware


from django.views.decorators.csrf import csrf_exempt




#For Login
class OrderView(View):
    @csrf_exempt

    def get(self , request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        orders = orders.reverse()
        print(orders)
        return render(request , 'orders.html', {'orders':orders})
   
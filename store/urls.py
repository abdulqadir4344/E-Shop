from django.contrib import admin
from django.urls import path
from . import views
from .views import Index
from .views import login , logout
from .views import signup
from .views import Cart
from .views import CheckOut
from .views import OrderView
from .middlewares.auth import auth_middleware







urlpatterns = [
    path('',Index.as_view() , name = 'homepage'),
    path('Signup',signup, name='signup'),
    path('login',login , name='login'),
    path('logout',logout , name='logout'),
    path('cart',Cart.as_view() , name='cart'),
    path('check-out',CheckOut.as_view() , name='checkout'),
    path('orders',auth_middleware(OrderView.as_view()) , name='orders'),

]
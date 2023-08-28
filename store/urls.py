from django.contrib import admin
from django.urls import path
from . import views
from .views import index
from .views import login , logout
from .views import signup
from .views import Cart
from .views import checkout
from .views import OrderView
from .middlewares.auth import auth_middleware







urlpatterns = [
    path('',index , name = 'homepage'),
    path('Signup',signup, name='signup'),
    path('login',login , name='login'),
    path('logout',logout , name='logout'),
    path('cart',Cart , name='cart'),
    path('check-out',checkout, name='checkout'),
    path('orders',auth_middleware(OrderView) , name='orders'),

]
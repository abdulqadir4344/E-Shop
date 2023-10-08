from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']   



# Register your models here.
admin.site.register(Session)
admin.site.register(Product , AdminProduct)
admin.site.register(Category , AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)

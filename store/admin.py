from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def AdminProduct(ModelAdmin):
    list_display = ['name','price','category']




# class AdminProduct(admin.ModelAdmin):
#     list_display = ['name','price','category']

@csrf_exempt
def AdminCategory(ModelAdmin):
    list_display = ['name']   

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)

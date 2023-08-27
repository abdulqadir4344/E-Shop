from django import template
from django.views.decorators.csrf import csrf_exempt

register = template.Library()


@register.filter(name='currency')

@csrf_exempt
def currency(number):
    return "₹"+str(number)

@register.filter(name='multiply')
@csrf_exempt
def multiply(number , number1):
    return number * number1


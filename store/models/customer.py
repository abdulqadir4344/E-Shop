from django.db import models
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField( max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return '%s %s' %(self.first_name,self.last_name)




    @csrf_exempt
    def register(self):
        self.save()

    @staticmethod
    @csrf_exempt
    def get_customer_by_email(email):
        try:

            return Customer.objects.get(email = email)
        except:
            return False


    @csrf_exempt
    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return  False


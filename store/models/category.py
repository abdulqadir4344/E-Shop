from django.db import models
from django.views.decorators.csrf import csrf_exempt

class Category(models.Model):
    name = models.CharField(max_length=20)



    @staticmethod
    @csrf_exempt
    def get_all_categories():
        return Category.objects.all()

    @csrf_exempt
    def __str__(self):
        return self.name




# added by me after changes 

    
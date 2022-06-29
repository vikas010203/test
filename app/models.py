from pyexpat import model
from django.db import models

# Create your models here.
class ECom(models.Model) :
    product_name = models.CharField(max_length=150);
    product_price = models.IntegerField();
    
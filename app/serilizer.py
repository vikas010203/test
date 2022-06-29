from .models import ECom
from rest_framework import serializers



class EcomSerilizer(serializers.ModelSerializer):
   """ School serializer for school model """
   class Meta:
      model= ECom
      fields= ['id','product_name',"product_price"]


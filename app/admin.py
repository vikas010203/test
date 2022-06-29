from django.contrib import admin

from app.models import ECom

# Register your models here.
@admin.register(ECom)

class ecomadmin(admin.ModelAdmin):
    list_display= ['id','product_name',"product_price"]
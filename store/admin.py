from category.models import Category
from django.contrib import admin
from django.db import models
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)} 
    list_display = ('product_name','price','stock','category','modified','is_available')
    
admin.site.register(Product,ProductAdmin)
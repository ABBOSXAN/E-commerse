from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Products, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
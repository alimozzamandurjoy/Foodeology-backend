from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    list_display = ['id','name','price','items']
@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ['id','catagory']

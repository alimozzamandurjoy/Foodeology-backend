from itertools import product
from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    item_objects= Item.objects.all()
    item_name= request.GET.get('item_name')

    # if item_name != '' and item_name is not None:
    #     item_objects= item_objects.filter(title__icontains= item_name)
    return render(request,'food/index.html',{'item_objects':item_objects})


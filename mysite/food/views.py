from itertools import product
from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    item_objects= Item.objects.all()
    item_title= request.GET.get('search')
    pizza= request.GET.get('P')

    if item_title != '' and item_title is not None:
        item_objects= item_objects.filter(name__icontains= item_title)
    
    return render(request,'food/index.html',{'item_objects':item_objects})


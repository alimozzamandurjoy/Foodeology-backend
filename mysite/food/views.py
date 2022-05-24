from itertools import product
from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    item_objects= Item.objects.all()
    
    cat= Cat.objects.all()
    # pizza=Cat.objects.filter(pk=1)
    # print(pizza)

    CATID= request.GET.get('catagories')
    if CATID:
        item_objects= Item.objects.filter(items= CATID)
    else:
        item_objects= Item.objects.all()


    #search 
    item_title= request.GET.get('search')
    if item_title != '' and item_title is not None:
        item_objects= item_objects.filter(name__icontains= item_title)
    
    return render(request,'food/index.html',{'item_objects':item_objects, 'cat':cat})

# def catagory(request,pk):
#     cat=Cat.objects.get(pk=pk)
    
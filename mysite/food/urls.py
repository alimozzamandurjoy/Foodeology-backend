from django.urls import URLPattern, path
from .import views
from .views import *

urlpatterns= [

    path("",views.index, name='index'),
    # path("cat/<int:pk>/",views.catagory,name="catagory"),
]
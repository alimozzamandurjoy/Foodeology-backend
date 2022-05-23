from django.db import models

# Create your models here.

CHOICES= (
    ('P','Pizza'),
    ('B','Burger'),
    ('R','Rice'),
    ('D','Dessert'),
    ('C','Coffee'),

)

class Cat(models.Model):
    catagory= models.CharField(max_length=20)
    def __str__(self):
        return self.catagory


class Item(models.Model):
    img= models.ImageField(upload_to='images')
    name= models.CharField(max_length=30)
    price= models.IntegerField()
    s_price= models.IntegerField()
    m_price= models.IntegerField()
    l_price= models.IntegerField()
    items= models.ForeignKey(Cat, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


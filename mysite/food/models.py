from django.db import models

# Create your models here.

CHOICES= (
    ('P','Pizza'),
    ('B','Burger'),
    ('R','Rice'),
    ('D','Dessert'),
    ('C','Coffee'),

)

class Item(models.Model):
    img= models.ImageField(upload_to='images')
    name= models.CharField(max_length=30)
    price= models.IntegerField()
    s_price= models.IntegerField()
    m_price= models.IntegerField()
    l_price= models.IntegerField()
    items= models.CharField(choices=CHOICES,max_length=100)
    def __str__(self):
        return self.name
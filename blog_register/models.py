from django.db import models

# Create your models here.

class Blog(models.Model):
    title= models.CharField(max_length=100)
    description= models.TextField()
    auth_name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='images/')
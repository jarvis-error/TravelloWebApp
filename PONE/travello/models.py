from distutils.command.upload import upload
from django.db import models

# Create your models here.
class destination(models.Model):
    
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)
from django.db import models
from django.contrib.auth.models import Permission



 
# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    country = models.CharField(max_length=50,blank=False,null=False)
    description = models.TextField(blank=True,null=True)
    best_time_to_visit = models.CharField(max_length=200,blank=True,null=True)
    category=models.CharField(default="Choose Destination",max_length=30, choices=(('Beach','Beach'), ('Mountain','Mountain'), ('City', 'City'),('Historical','Historical')))
    image = models.URLField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
 

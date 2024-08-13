from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Parcel(models.Model):
  host = models.ForeignKey(User,on_delete=models.CASCADE)
  pickup_location=models.CharField(max_length=200)
  delivery_location=models.CharField(max_length=200)
  parcel_weight = models.CharField(max_length=40)
  parcel_size = models.CharField(max_length=60)
  parcel_contents=models.TextField(null=False,blank=False)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  class Meta:
    ordering = ['-updated','-created']
  def __str__(self):
    return 'To '+ self.delivery_location
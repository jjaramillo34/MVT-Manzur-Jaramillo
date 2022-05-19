from django.db import models
from datetime import datetime
# Create your models here.

class Family(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='images')
    is_desease = models.BooleanField(default=False)
    has_kids = models.BooleanField(default=False)
    kids_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=datetime.now())
    modified_at = models.DateTimeField(auto_now=True)
    sex = models.CharField(max_length=1, choices=SEX)
    title = models.CharField(max_length=25)
    dob = models.DateField()
    

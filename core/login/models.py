from django.db import models

# Create your models here.
from django.db import models

from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models
User= get_user_model()

class RegisterUser(models.Model):
    name= models.CharField(max_length=100)
    password1= models.TextField()
    password2= models.TextField(blank=True)
   
   
    def __str__(self):
        return self.name

class LoginUser(models.Model):
    name= models.CharField(max_length=100)
    password= models.TextField()
    def __str__(self):
        return self.name
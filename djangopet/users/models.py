from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(models.Model):
    
    gender = (
        ('female', 'женщина'),
        ('male', 'мужчина')
    )
    
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(choices=gender, max_length=50)
    avatar = models.ImageField(upload_to = 'djangopet/media/images')

    def __str__(self):
        return self.last_name
        


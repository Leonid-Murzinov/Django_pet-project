from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    
    gender = (
        ('female', 'женщина'),
        ('male', 'мужчина')
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=gender, max_length=50)
    avatar = models.ImageField(upload_to = 'djangopet/media/images')

    def __str__(self):
        return self.last_name
        

    
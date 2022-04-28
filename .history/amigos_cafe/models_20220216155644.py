from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=80)
    phone = models.CharField(max_length=10)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=5)
    members = models.CharField(max_length=2)  
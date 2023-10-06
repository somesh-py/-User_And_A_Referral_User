from django.db import models
# Create your models here.


class UserProfile(models.Model):
    username =  models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=500)
    referral_code = models.CharField(max_length=10, unique=True)
    referral_person_code = models.CharField(max_length=10,null=True, blank=True)
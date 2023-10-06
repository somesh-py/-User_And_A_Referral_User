from django.contrib import admin
from .models import UserProfile
# Register your models here.

@admin.register((UserProfile))
class UserProfileadminmodel(admin.ModelAdmin):
    list_display=['id','username','email','password','referral_code','referral_person_code']
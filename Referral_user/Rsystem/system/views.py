from django.shortcuts import render,redirect
from .models import UserProfile
from django.contrib.auth.hashers import make_password,check_password
import math,random

def registration(request):
    return render(request,'registration.html')


def registration_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        referral_code = request.POST.get('referral_code')


        if UserProfile.objects.filter(email=email).exists():
            return render(request, 'registration.html', {'msgs': 'Email already registered'})
        else:
            if referral_code:
                referred_by_user_profile = UserProfile.objects.filter(referral_code=referral_code).first()
                if referred_by_user_profile:

                    user_profile = UserProfile(username=username, email=email, password=make_password(password))
                    user_profile.referral_person_code = referred_by_user_profile.referral_code
                    user_profile.referral_code = get_new_referral_code()
                    user_profile.save()

                    return render(request, 'login.html')
                else:
                    return render(request, 'registration.html', {'msgs': 'Referral code was incorrect'})
            else:
                referral_code = get_new_referral_code()
                user_profile = UserProfile(username=username, email=email, password=make_password(password), referral_code=referral_code)
                user_profile.save()
                return render(request, 'login.html')

    else:
        return render(request, 'registration/register.html')

def get_new_referral_code():
    digits="0123456789"
    new_referrel_code=""
    for i in range(5):
        new_referrel_code+=digits[math.floor(random.random()*10)]
    return new_referrel_code

def login(request):
    return render(request,'login.html')


def login_request(request):
    if request.method == 'POST':
        Login_email = request.POST.get('email')
        Login_password = request.POST.get('password')

        try:
            user_db_instance = UserProfile.objects.get(email=Login_email)
        except UserProfile.DoesNotExist:
            return render(request, 'login.html', {'msgs': 'Email not found'})

        user_db_password = user_db_instance.password

        if check_password(Login_password, user_db_password):
            try:
                referral_person_code_one = user_db_instance.referral_person_code
                referral_person = UserProfile.objects.get(referral_code=referral_person_code_one)
                return render(request,'dashboard.html', {'user': user_db_instance, 'referral_person': referral_person})
            except UserProfile.DoesNotExist:
                return render(request,'dashboard.html', {'user': user_db_instance})
        else:
            return render(request, 'login.html', {'msgs': 'Password was incorrect'})

    return render(request, 'login.html')

def dashboard(request):
    return render(request,'dashboard.html')
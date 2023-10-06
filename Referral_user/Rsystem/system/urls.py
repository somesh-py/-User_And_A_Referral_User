from django.urls import path
from . import views


urlpatterns = [
    path('',views.registration),
    path('registration_request/',views.registration_request),
    path('login/',views.login),
    path('login_request/',views.login_request),
    path('dashboard/',views.dashboard),
]

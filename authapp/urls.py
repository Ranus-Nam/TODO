from django.urls import path
from . import views
from .views import *

app_name = 'authapp'

urlpatterns = [
    path('', login_view, name='login'),  
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard')
    ]

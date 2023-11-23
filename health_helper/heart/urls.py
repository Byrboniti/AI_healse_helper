
from django.urls import path
from .views import heart_home

urlpatterns = [
    path('', heart_home, name='predict'),

]

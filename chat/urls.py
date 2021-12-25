# chat/urls.py
from django.urls import path

from .views import index , room , unauthorized 

app_name='chat'

urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', room , name='room'),

    
    path('unauthorized' , unauthorized , name = 'unauthorized')
]
from django.urls import path
from .views import index, records, chat

urlpatterns = [
    path('index/', index),
    path('records/', records),
    path('chat/', chat, name='chat')
]
from django.urls import path
from .views import chat, login_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('chat/', chat, name='chat'),
    path('', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


# urlpatterns = [
#     path('chat/', chat, name='chat'),
#     path('', login_view, name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# ]
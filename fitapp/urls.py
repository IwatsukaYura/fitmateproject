from . import views
from django.urls import path
from .views import Welcome, Dashbord

urlpatterns = [
    path('welcome/', Welcome.as_view() ,name='welcome'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('user/', views.user_view, name='user'),
    path('dashbord/', Dashbord.as_view() ,name='dashbord'),
]
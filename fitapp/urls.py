from . import views
from django.urls import path
from .views import Welcome, Start

urlpatterns = [
    path('welcome/', Welcome.as_view() ,name='welcome'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('user/', views.user_view, name='user'),
    path('dashbord/', views.dashbord_view ,name='dashbord'),
    path('start/', Start.as_view() ,name='start'),
    path('weight/', views.weight_view ,name='weight'),
]
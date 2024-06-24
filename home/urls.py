from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('home/',views.home,name='home'),
    path('login/',views.loginuser,name='login'),
    path('customregestion/',views.customeruser,name='customerregestion'),
    path('forget/',views.passwordchange,name='forget'),
    path('profile/',views.profile,name='profile'),
]

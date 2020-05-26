from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('p1/',views.p1,name='p1'),
    path('logout/',views.user_logout,name='logout'),
    
]
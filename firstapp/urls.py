from django.urls import path
from firstapp.views import home,userlogin,userlogout,signup,profile,change_pass,change_pass2
urlpatterns = [
    path('',home,name='homepage'),
    path('login/',userlogin,name='login'),
    path('logout/',userlogout,name='logout'),
    path('signup/',signup,name ='signup'),
    path('change_password/',change_pass,name ='change_pass'),
    path('change_password_without_old/',change_pass2,name ='change_pass2'),
    path('profile/',profile,name ='profile'),
    
]

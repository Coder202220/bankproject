from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('login/login',views.login,name='login'),
    path('applybutton',views.applybutton,name='applybutton'),
    path('applyform',views.applyform,name='applyform'),
    # path('message',views.message1,name='message'),
    path('logout',views.logout,name='logout'),
]
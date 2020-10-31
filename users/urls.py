"""
@author mdark1001 | Miguel Cabrera R. <miguel.cabrera.app@gmail.com>
@date 26/10/20
@project 
@name urls
"""
from django.urls import path

from .views import LoginView, LogoutView, SignupView, UpdateProfileView

urlpatterns = [
    # path('',views.home,name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('me/profile/', UpdateProfileView.as_view(), name='profile'),

]

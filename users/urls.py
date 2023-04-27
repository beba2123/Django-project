from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userlogin, name="login"),
    path('logout/', views.userlogout, name="logout"),
    path('register/', views.registeruser, name="register"),
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>', views.userProfile, name="user-profile"),
    path('account/', views.userAccount, name="account"),

    path('edit-account/', views.editAccount, name="edit-account"),
    path('create-skill/', views.createSkill, name="create-skill"),
]

from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.profiles, name="profiles"),
    path('update-skill/<str:pk>/', views.updateSkill, name="update-skill"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('register/', views.registerUser, name="register"),
    path('account/', views.userAccount, name="account"),
    path('edit-account/', views.editAccount, name="edit-account"),
    path('create-skill/', views.createSkill, name="create-skill"),
    path('delete-skill/<str:pk>/', views.deleteSkill, name="delete-skill"),
    path('cancel-delete/', views.cancel_delete, name='cancel-delete'),
    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.viewMessage, name="message"),
    path('create-message/<str:pk>/', views.createMessage, name="create-message"),

    
]


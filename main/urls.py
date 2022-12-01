from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainPage , name='main'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('friends/', views.friends, name='friends'),
    path('createrelationship/<profile_id>/', views.create_relationship, name='create_relationship')
]

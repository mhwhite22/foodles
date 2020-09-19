from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipe/', views.RecipeList.as_view(), name='recipe'),
    path('accounts/signup/', views.signup, name='signup'),
]
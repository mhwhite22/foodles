from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipe/', views.RecipeList.as_view(), name='recipes_index'),
    path('recipe/<int:pk>/', views.RecipeDetail.as_view(), name='recipes_detail'),
    path('recipe/create/', views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipe/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipe/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('meals/', views.MealList.as_view(), name='meals_index'),
    path('meals/<int:pk>/', views.MealDetail.as_view(), name='meals_detail'),
]
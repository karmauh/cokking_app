from django.contrib import admin
from django.urls import path
from .views import HomeView, RecipesView, EditRecipeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recipes/', RecipesView.as_view(), name='recipes'),
    path('edit_recipe/<int:pk>', EditRecipeView.as_view(), name='edit_recipe'),
]
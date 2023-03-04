from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from .models import CookBook
from .forms import EditRecipeForm
from django.urls import reverse_lazy

# Create your views here.
class HomeView(ListView):
    model = CookBook
    template_name = 'home.html'
    
class RecipesView(ListView):
    model = CookBook
    template_name = 'all_recipes.html'
    context_object_name = 'cook_items'
    ordering = ['-id']
    
class EditRecipeView(UpdateView):
    model = CookBook
    form_class = EditRecipeForm
    template_name = 'edit_recipe.html'
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')
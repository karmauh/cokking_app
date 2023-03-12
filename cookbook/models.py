from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class CookBook(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)
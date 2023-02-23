from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class CookBook(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)
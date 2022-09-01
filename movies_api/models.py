from django.contrib.auth import get_user_model
from django.db import models


class Movies(models.Model):
    class Meta:
        verbose_name_plural = 'MOVIE'
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.

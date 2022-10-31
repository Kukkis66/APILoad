from django.db import models
from django.contrib import auth

class Filemodel(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='')
    time = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.title



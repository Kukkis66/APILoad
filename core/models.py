from django.db import models
from django.contrib import auth

class Filemodel(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='')
    time = models.DateTimeField(auto_now_add=True)
    downloads = models.PositiveIntegerField(default=0)


    def download_counter(self):
        self.downloads += 1
    
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    def __str__(self) -> str:
        return self.title



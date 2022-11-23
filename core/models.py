from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    organization = models.CharField(max_length=40, unique=True)



#model for file
class Filemodel(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='')
    time = models.DateTimeField(auto_now_add=True)
    downloads = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)


    def download_counter(self):
        self.downloads += 1
    
    #delete function what deletes physical file from /media folder
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    def __str__(self) -> str:
        return self.title



from django.db import models

class Filemodel(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='')
    time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title



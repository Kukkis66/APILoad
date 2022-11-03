from typing import Collection
from rest_framework import serializers

from .models import Filemodel

class FileSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    file = serializers.FileField()
    class Meta:
        model = Filemodel
        fields = ['id', 'title', 'file', 'time',]
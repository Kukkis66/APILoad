from rest_framework import serializers

from .models import Filemodel

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filemodel
        fields = ['id', 'title', 'time', 'file']
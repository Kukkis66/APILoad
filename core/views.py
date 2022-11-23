from django.shortcuts import render, redirect



from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from . serializers import FileSerializer
from . forms import SignUpForm
from . models import Filemodel


#Viewset for files
class FileViewSet(ModelViewSet):
    queryset = Filemodel.objects.all()
    serializer_class = FileSerializer
    permission_classes = ( IsAuthenticated, )










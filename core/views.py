from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view

from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import FileSerializer



from .models import Filemodel


class FileViewSet(ModelViewSet):
    queryset = Filemodel.objects.all()
    serializer_class = FileSerializer
    permission_classes = ( IsAuthenticated, )





# class FileList(APIView):
#     def get(self, request, id):
#         file = get_object_or_404(Filemodel, pk=id)
#         serializer = FileSerializer(file)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = FileSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)




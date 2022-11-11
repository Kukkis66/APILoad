from django.shortcuts import render, redirect



from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from . serializers import FileSerializer
from . forms import SignUpForm
from . models import Filemodel

import os


class FileViewSet(ModelViewSet):
    queryset = Filemodel.objects.all()
    serializer_class = FileSerializer
    permission_classes = ( IsAuthenticated, )


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})




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




from users.models import Design
from users.serializers import  UploadDesignSerializer
from rest_framework import generics


class UploadDesign(generics.ListCreateAPIView):
    queryset = Design.objects.all()
    serializer_class =  UploadDesignSerializer


class DesignDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Design.objects.all()
    serializer_class =  UploadDesignSerializer

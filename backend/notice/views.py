from django.shortcuts import render
from rest_framework import generics

from .models import Notice
from .serializers import NoticeSerializer

class ListNotice(generics.ListCreateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
class DetailNotice(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
# Create your views here.

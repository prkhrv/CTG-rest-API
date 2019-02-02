from django.shortcuts import render
from rest_framework import viewsets,mixins
from .models import getintouch
from .serializers import GetintouchSerializer

# Create your views here.

class GetinTouchView(mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = getintouch.objects.all()
    serializer_class = GetintouchSerializer

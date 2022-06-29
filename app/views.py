from django.shortcuts import render
from rest_framework import viewsets
from .serilizer import EcomSerilizer
from .models import ECom

class UserView(viewsets.ModelViewSet):
    serializer_class = EcomSerilizer
    queryset = ECom.objects.all()
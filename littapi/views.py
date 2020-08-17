from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LmsSerializer
from .models import Lms


class LmsViewSet(viewsets.ModelViewSet):
    queryset = Lms.objects.all().order_by('name')
    serializer_class = LmsSerializer

# Create your views here.

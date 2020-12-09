from django.shortcuts import render
from rest_framework import viewsets 
from .models import Chicken
from .serializers import ChickenSerializer

# Create your views here.
class ChickenViewSet(viewsets.ModelViewSet):
    queryset = Chicken.objects.all()
    serializer_class = ChickenSerializer
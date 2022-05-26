from django.shortcuts import render
from rest_framework import generics
from incidents.models import Incident
from.serializers import IncidentSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class APIList(generics.ListCreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class APIDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
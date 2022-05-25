from django.shortcuts import render

from django.urls import path
from .views import (
    HomeListView,
    HomeDetailView,
    HomeCreateView,
    HomeUpdateView,
    HomeDeleteView
)

urlpatterns = [
    path('<int:pk>/delete/', HomeDeleteView.as_view(), name='incidents/incident_delete'),
    path('<int:pk>/edit/', HomeUpdateView.as_view(), name='incidents/incident_edit'),
    path('new/', HomeCreateView.as_view(), name='incidents/incident_new'),
    path('<int:pk>/', HomeDetailView.as_view(), name='incidents/incident_detail'),
    path('', HomeListView.as_view(), name='incidents/incident_list'),
]
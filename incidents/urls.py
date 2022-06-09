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

    # Delete Incident URL
    path('<int:pk>/delete/', HomeDeleteView.as_view(), name='incidents/incident_delete'),

    # Update Incident URL
    path('<int:pk>/edit/', HomeUpdateView.as_view(), name='incidents/incident_edit'),

    # New Incident URL
    path('new/', HomeCreateView.as_view(), name='incidents/incident_new'),

    # Detailed URL by PK Key
    path('<int:pk>/', HomeDetailView.as_view(), name='incidents/incident_detail'),

    # Incident List URL
    path('', HomeListView.as_view(), name='incidents/incident_list'),
]

from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Incident
# Create your views here.

class HomeListView(ListView):
    model = Incident
    template_name = 'incidents/incident_list.html'


class HomeDetailView(DetailView):
    model = Incident
    template_name = 'incidents/incident_detail.html'

class HomeCreateView(CreateView):
    model = Incident
    template_name = 'incidents/incident_new.html'
    fields = ['full_name', 'team', 'organization_impacted_by_incident', 'incident_discovery_method',
               'affiliation_to_org', 'user_incident_reported_by', 'employee_email',
              'customer_email', 'prevention', 'additional_notes']

class HomeUpdateView(UpdateView):
    model = Incident
    template_name = 'incidents/incident_edit.html'
    fields = ['full_name', 'team', 'organization_impacted_by_incident', 'incident_discovery_method',
              'affiliation_to_org', 'user_incident_reported_by', 'employee_email',
              'customer_email', 'prevention', 'additional_notes']

class HomeDeleteView(DeleteView):
    model = Incident
    template_name = 'incidents/incident_delete.html'
    success_url = reverse_lazy('home')


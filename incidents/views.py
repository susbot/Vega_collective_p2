from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Incident

# Create your views here.

class HomeListView(LoginRequiredMixin, ListView):
    model = Incident
    template_name = 'incidents/incident_list.html'


class HomeDetailView(LoginRequiredMixin, DetailView):
    model = Incident
    template_name = 'incidents/incident_detail.html'

class HomeCreateView(LoginRequiredMixin, CreateView):
    model = Incident
    template_name = 'incidents/incident_new.html'
    fields = ['what_happened', 'customer_id', 'customer_email', 'how_was_it_discovered',
              'how_could_we_have_prevented_this', 'additional_notes', 'data_of_incident', 'author']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class HomeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Incident
    template_name = 'incidents/incident_edit.html'
    fields = ['what_happened', 'customer_id', 'customer_email','how_was_it_discovered',
              'how_could_we_have_prevented_this', 'additional_notes', 'data_of_incident', 'author']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class HomeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Incident
    template_name = 'incidents/incident_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user




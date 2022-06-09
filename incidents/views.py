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
from incidents.models import Incident


# [LoginRequiredMixin] added to restrict view access to only logged-in users
# Class for the ListView functionality
class HomeListView(LoginRequiredMixin, ListView):
    model = Incident
    template_name = 'incidents/incident_list.html'


# [LoginRequiredMixin] added to restrict view access to only logged-in users
# Class for the DetailView functionality
class HomeDetailView(LoginRequiredMixin, DetailView):
    model = Incident
    template_name = 'incidents/incident_detail.html'


# [LoginRequiredMixin] added to restrict view access to only logged-in users
# class for the CreateView functionality
class HomeCreateView(LoginRequiredMixin, CreateView):
    model = Incident
    template_name = 'incidents/incident_new.html'
    fields = ['what_happened', 'customer_id', 'customer_email', 'how_was_it_discovered',
              'how_could_we_have_prevented_this', 'additional_notes', 'data_of_incident', 'level']

    # Create a function that automatically sets the author field.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# [LoginRequiredMixin] added to restrict view access to only logged-in users
# Class for the UpdateView functionality
class HomeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Incident
    template_name = 'incidents/incident_edit.html'
    fields = ['what_happened', 'customer_id', 'customer_email', 'how_was_it_discovered',
              'how_could_we_have_prevented_this', 'additional_notes', 'data_of_incident', 'level']

    # [UserPassesTestMixin] Restricts access so only the author of the Incident has permission to Update or Delete
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# [LoginRequiredMixin] added to restrict view access to only logged-in users
# Class for the DeleteView functionality
class HomeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Incident
    template_name = 'incidents/incident_delete.html'
    success_url = reverse_lazy('home')

    # [UserPassesTestMixin] Restricts access so only the author of the Incident has permission to Update or Delete
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
# Create your models here.
incident_type = (
    ("Inadvertent Data Exposure", "Inadvertant Data Exposure"),
    ("Security Misconfiguration", "Security Misconfiguration"),
    ("Product Vulnerability", "Product Vulnerability"),
    ("Vendor Incident", "Vendor Incident"),
)
severity = (
    ("Low", "Low"),
    ("Medium", "Medium"),
    ("High", "High"),
    ("Critical", "Critical"),
)

class Incident(models.Model):
    what_happened = models.CharField(max_length=40, choices=incident_type)
    customer_id = models.CharField(max_length=15)
    customer_email = models.EmailField()
    when_did_it_happen = models.DateField(auto_now_add=True, editable=False)
    how_was_it_discovered = models.TextField()
    how_could_we_have_prevented_this = models.TextField()
    additional_notes = models.TextField()
    data_of_incident = models.DateField(auto_now=False)
    level = models.CharField(max_length=20, choices=severity)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        editable=True,
    )


    def __str__(self):
        return self.customer_id[:50]

    def get_absolute_url(self):
        return reverse('incidents/incident_detail', args=[str(self.id)])
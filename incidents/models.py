
from django.db import models
from django.urls import reverse
# Create your models here.
class Incident(models.Model):
    full_name = models.CharField(max_length=50)
    team = models.CharField(max_length=20)
    organization_impacted_by_incident = models.CharField(max_length=20)
    incident_discovery_method = models.TextField()
    affiliation_to_org = models.CharField(max_length=30)
    user_incident_reported_by = models.CharField(max_length=20)
    employee_email = models.EmailField()
    customer_email = models.EmailField()
    prevention = models.TextField()
    additional_notes = models.TextField()
    date_incident_reported = models.DateField(auto_now_add=True, editable=True)
    date_incident_occured = models.DateField(auto_now=False)


    def __str__(self):
        return self.organization_impacted_by_incident[:50]

    def get_absolute_url(self):
        return reverse('incident_detail', args=[str(self.id)])
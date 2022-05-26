from rest_framework import serializers
from incidents.models import Incident

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ('full_name', 'employee_email', 'customer_email', 'author',)
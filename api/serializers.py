from rest_framework import serializers
from incidents.models import Incident

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ['what_happened', 'customer_id', 'customer_email', 'how_was_it_discovered',
                  'how_could_we_have_prevented_this', 'additional_notes', 'data_of_incident', 'level']



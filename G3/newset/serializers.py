from newset.models import NewsetStudent
from rest_framework import serializers


class NewsetStudentSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = NewsetStudent
        fields = ['id', 'name', 'roll', 'city']
from concrete.models import ConcreteStudent
from rest_framework import serializers


class ConcreteStudentSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = ConcreteStudent
        fields = ['id', 'name', 'roll', 'city']
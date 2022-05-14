from operator import imod
from rest_framework import serializers
from .models import Student

#       Serialization / Get Data

class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)



#       Deserialization / Post Data

    def create(self, validate_data):
        return Student.objects.create(**validate_data)
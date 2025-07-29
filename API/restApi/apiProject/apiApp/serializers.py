from rest_framework import serializers
from apiApp.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'
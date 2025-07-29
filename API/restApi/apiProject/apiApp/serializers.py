from rest_framework import serializers
from apiApp.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'


    # def create(self, validated_data):
    #     instance = StudentModel.objects.create(**validated_data)
    #     instance.student_roll = 2
    #     instance.save()
    #     return instance

    def create(self, validated_data):
        name = validated_data.get('student_name')
        student = StudentModel.objects.order_by('-student_roll').first()
        if student:
            roll = student.student_roll + 1
        else:
            roll = 1

        student_data = StudentModel.objects.create(**validated_data)
        student_data.student_roll = roll
        student_data.username = (name + str(roll)).lower()
        student_data.save()
        return student_data
from django.shortcuts import render
from apiApp.models import *
from apiApp.serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def studentList(request):
    if request.method == 'GET':
        student_data = StudentModel.objects.all()
        serializer = StudentSerializer(student_data, many=True)
        return Response({
            'success': True,
            'message': 'Student data list successfully fetched',
            'data': serializer.data,
        }, status=status.HTTP_200_OK)

    else:
        return Response({
            'success': False,
            'message': 'Student data not fetched',
        }, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def addStudent(request):
    if request.method == 'POST':
        student_serializer = StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()

            return Response({
            'success': True,
            'message': 'Student data list successfully Added',
            'data': student_serializer.data,
        }, status=status.HTTP_200_OK)

    else:
        return Response({
            'success': False,
            'message': 'Student data not Added',
        }, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def editStudent(request,pk):
    student = StudentModel.objects.get(id=pk)
    student_serializer = StudentSerializer(student, data = request.data, partial=True)
    if student_serializer.is_valid():
        student_serializer.save()
        return Response(student_serializer.data)
    else:
        return Response(student_serializer.errors)
    
@api_view(['DELETE'])
def deleteStudent(request,pk):
    StudentModel.objects.get(id=pk).delete()
    return Response({
        "message":"Data deleted successfully"
    })



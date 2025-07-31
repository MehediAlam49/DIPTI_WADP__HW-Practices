from django.shortcuts import render
from crudApp.models import *
from crudApp.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def productList(request):
    if request.method == 'GET':
        product = ProductModel.objects.all()
        serializer = ProductSerializer(product,many=True)
        return Response({
            'success': True,
            'message': 'Product list successfully fetched',
            'data': serializer.data,
        }, status=status.HTTP_200_OK)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from crudApp.models import ProductModel
from crudApp.serializers import ProductSerializer

# GET (list) and POST (create)
@api_view(['GET', 'POST'])
def product_list_create(request):
    if request.method == 'GET':
        products = ProductModel.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({
            'success': True,
            'message': 'Product list fetched successfully',
            'data': serializer.data,
        }, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Product created successfully',
                'data': serializer.data,
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'message': 'Product creation failed',
            'errors': serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)


# GET (retrieve), PUT (update), DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = ProductModel.objects.get(pk=pk)
    except ProductModel.DoesNotExist:
        return Response({
            'success': False,
            'message': 'Product not found',
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response({
            'success': True,
            'message': 'Product retrieved successfully',
            'data': serializer.data,
        }, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Product updated successfully',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'message': 'Product update failed',
            'errors': serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response({
            'success': True,
            'message': 'Product deleted successfully',
        })

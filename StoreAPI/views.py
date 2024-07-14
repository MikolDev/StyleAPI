from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


# Create your views here.
class CategoryListApiView(APIView):
    def get(self, request, *args, **kwargs):
        # Get all categories
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        # Get a category by id
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get_by_id(self, request, pk, *args, **kwargs):
        # Get a category by id
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class ProductListApiView(APIView):
    def get(self, request, *args, **kwargs):
        # Get all products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        # Get a product by id
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get_by_id(self, request, pk, *args, **kwargs):
        # Get a product by id
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
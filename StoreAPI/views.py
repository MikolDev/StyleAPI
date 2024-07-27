from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend


class CategoryListApiView(APIView):

    # List all categories
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

    # Create category
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'image': request.data.get('image')
        }
        serializer = CategorySerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class CategoryDetailApiView(APIView):

    # Helper method - Get category by ID
    def get_object(self, category_id):
        try:
            return Category.objects.get(id = category_id)
        except Category.DoesNotExist:
            return None
    

        # Get category
    def get(self, request, category_id, *args, **kwargs):
        category_instance = self.get_object(category_id)

        if not category_instance:
            return Response(
                { "res": "Category with such ID does not exist." },
                status = status.HTTP_400_BAD_REQUEST
            )

        serializer = CategorySerializer(category_instance)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

    # Update category
    def put(self, request, category_id, *args, **kwargs):
        category_instance = self.get_object(category_id)

        if not category_instance:
            return Response(
                { "res": "Category with such ID does not exist." },
                status = status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'name': request.data.get('name'),
            'image': request.data.get('image')
        }

        serializer = CategorySerializer(instance = category_instance, data = data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    # Delete category
    def delete(self, request, category_id, *args, **kwargs):
        category_instance = self.get_object(category_id)

        if not category_instance:
            return Response(
                { "res": "Category with such ID does not exist." },
                status = status.HTTP_400_BAD_REQUEST
            )
        
        category_instance.delete()

        return Response(
            { 'res': 'Category deleted.' },
            status = status.HTTP_200_OK
        )


class ProductListApiView(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    # List all products
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()

        # Category ID filter
        filterset = self.filterset_class(request.GET, queryset=products)
        if filterset.is_valid():
            products = filterset.qs

        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

    # Create product
    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'price': request.data.get('price'),
            'description': request.data.get('description'),
            'image': request.data.get('image'),
            'category': request.data.get('category')
        }
        serializer = ProductSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ProductDetailApiView(APIView):

    # Helper method - Get product by ID
    def get_object(self, product_id):
        try:
            return Product.objects.get(id = product_id)
        except Product.DoesNotExist:
            return None
    

        # Get product
    def get(self, request, product_id, *args, **kwargs):
        product_instance = self.get_object(product_id)

        if not product_instance:
            return Response(
                { "res": "Product with such ID does not exist." },
                status = status.HTTP_400_BAD_REQUEST
            )

        serializer = ProductSerializer(product_instance)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

    # Update product
    def put(self, request, product_id, *args, **kwargs):
        product_instance = self.get_object(product_id)

        if not product_instance:
            return Response(
                { "res": "Product with such ID does not exist." },
                status = status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'title': request.data.get('title'),
            'price': request.data.get('price'),
            'description': request.data.get('description'),
            'image': request.data.get('image'),
            'category': request.data.get('category')
        }

        serializer = ProductSerializer(instance = product_instance, data = data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    # Delete product
    def delete(self, request, product_id, *args, **kwargs):
        product_instance = self.get_object(product_id)

        if not product_instance:
            return Response(
                { "res": "Product with such ID does not exist." },
                status = status.HTTP_400_BAD_REQUEST
            )
        
        product_instance.delete()

        return Response(
            { 'res': 'Product deleted.' },
            status = status.HTTP_200_OK
        )

from django.urls import path
from .views import CategoryListApiView, ProductListApiView

urlpatterns = [
    path('categories/', CategoryListApiView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryListApiView.as_view(), name='category-detail'),
    path('products/', ProductListApiView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductListApiView.as_view(), name='product-detail'),
]
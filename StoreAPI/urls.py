from django.urls import path
from .views import CategoryListApiView, CategoryDetailApiView, ProductListApiView, ProductDetailApiView

urlpatterns = [
    path('categories/', CategoryListApiView.as_view(), name='category-list'),
    path('categories/<int:category_id>/', CategoryDetailApiView.as_view(), name='category-detail'),
    path('products/', ProductListApiView.as_view(), name='product-list'),
    path('products/<int:product_id>/', ProductDetailApiView.as_view(), name='product-detail')
]
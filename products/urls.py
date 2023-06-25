from django.urls import path, include
from rest_framework import routers

from products.serializer import ProductListByCategoryAPIView
from .views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/<str:category_slug>/', ProductListByCategoryAPIView.as_view(), name='product-list-by-category'),
]

from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, filters
from .serializer import ProductSerializer, CategorySerializer
from .models import Product, Category
from .forms import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering and pagination."""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
            )
    permission_classes = (
        permissions.IsAuthenticated,
        #TokenHasReadWriteScope,
        )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
            )    


class ProductViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing Products."""
    
    queryset = Product.objects.order_by('name',) 
    serializer_class = ProductSerializer   
    filter_class = ProductFilter
    search_fields = ('name','price')
    ordering_fields = ('price','name','total_available')

    
class CategoryViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing Category."""
    
    queryset = Category.objects.order_by('-name',) 
    serializer_class = CategorySerializer   
    search_fields = ('name',)
    



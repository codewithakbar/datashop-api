from django.contrib.auth import get_user_model
import requests
from rest_framework import authentication, permissions, viewsets, filters, generics
from .serializer import ProductSerializer, CategorySerializer
from .models import Product, Category
from .forms import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.http import HttpResponse

from config.config import BOT_TOKEN

class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering and pagination."""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
            )
    permission_classes = (
        # permissions.IsAuthenticated,
        # permissions.IsAuthenticatedOrReadOnly
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
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Product.objects.order_by('name',).filter(parent=None)
    serializer_class = ProductSerializer   
    filter_class = ProductFilter
    search_fields = ('name','price')
    ordering_fields = ('price','name','total_available')


class CategoryViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing Category."""
    permission_classes = [IsAuthenticatedOrReadOnly]


    queryset = Category.objects.order_by('-name',).filter(parent=None)
    serializer_class = CategorySerializer   
    search_fields = ('name',)
    

class ProductListByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return Product.objects.filter(category__slug=category_slug)


def home(request):
    user_id = '984573662'
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    ip_address = request.META.get('REMOTE_ADDR')

    params = {
        "chat_id": user_id,
        "text": ip_address
    }

    response = requests.post(url, params=params)

    return HttpResponse(f'<b>Hello, world!<br><br>{ip_address}</b>')
    
    

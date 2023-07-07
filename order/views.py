from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSerializer
from .models import Order

from rest_framework import permissions


class OrderSetView(ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(user=user).order_by('-id') 
        return queryset

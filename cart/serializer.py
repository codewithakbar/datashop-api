from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse

from products.models import Images
from .models import Cart



User = get_user_model()


class CartSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    products = serializers.SerializerMethodField('get_products')

    class Meta:
        model = Cart
        fields = ['id', 'product', 'user', 'quantity', 'links', 'products']

    def get_links(self, obj):
        request = self.context['request']
        links = {
            'self': reverse('cart-detail', kwargs={'pk': obj.pk}, request=request),
            'shopper': None,
            'purchases': None,
        }
        if obj.product:
            links['purchases'] = reverse('product-detail', kwargs={'pk': obj.product.pk}, request=request)
        return links

    def get_products(self, obj):
        products = []
        if obj.product:
            product_data = {
                'id': obj.product.id,
                'name': obj.product.name,
                'price': obj.product.price,
                'images': self.get_product_images(obj.product.id)
            }
            products.append(product_data)
        return products

    def get_product_images(self, product_id):
        images = Images.objects.filter(product_id=product_id)
        if images:
            return [image.image.url for image in images]
        return []


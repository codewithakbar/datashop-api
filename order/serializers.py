from rest_framework import serializers

from products.models import Images
from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField('get_products')

    class Meta:
        model = Order
        fields = '__all__'


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
            return [image.image.url for image in images[:1]]
        return []
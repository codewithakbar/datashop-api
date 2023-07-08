from rest_framework import serializers

from products.models import Images
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    # product = serializers.SerializerMethodField('get_products')

    class Meta:
        model = Order
        fields = (
            'user', 'product', 'dostavka', 'country', 'city',
            'address', 'pay_metod', 'first_name', 'last_name',
            'phone' 
        )


    # def get_products(self, obj):
    #     products = []
    #     cart = obj.product
    #     if cart:
    #         product_data = {
    #             'id': cart.id,
    #             'name': cart.product.name,
    #             # 'price': cart.product.price,
    #             # 'images': self.get_product_images(cart.product.id)
    #         }
    #         products.append(product_data)
    #     return products




    
    def get_product_images(self, product_id):
        images = Images.objects.filter(product_id=product_id)
        if images:
            return [image.image.url for image in images[:1]]
        return []
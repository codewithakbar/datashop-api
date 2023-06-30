from django.contrib.auth import get_user_model
from django.db.models import Prefetch
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product, Images, ProductComment, Category, ImageUpload, Xususiyatlari
from drf_writable_nested import WritableNestedModelSerializer


User = get_user_model()



class CategorySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField('get_links')

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'links', 'children']

    def get_children(self, obj):
        child_categories = obj.children.all()
        child_serializer = CategorySerializer(child_categories, many=True)
        return child_serializer.data
    
    def get_links(self, obj):
        request = self.context.get('request')
        links = {
            'self': reverse('category-detail', kwargs={'pk': obj.pk}, request=request),
        }
        return links



class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = "__all__"



class ProductImageSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Images
        fields = ("image", )



class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = "__all__"



class XususiyatlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xususiyatlari
        fields = ['title', 'desc']


class ProductSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    category = serializers.SerializerMethodField()
    images = ProductImageSerializer(many=True)
    product_comments = ProductCommentSerializer(read_only=False)
    xususiyatlari = XususiyatlariSerializer(many=True)


    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'price', 'total_available', 'total_count', 'product_comments', 'links', 'xususiyatlari', 'description', 'images',]

    def get_links(self, obj):
        request = self.context['request']
        links = {
            'self': reverse('product-detail', kwargs={'pk': obj.pk}, request=request),
        }
        return links

    def get_category(self, obj):
        product_category = obj.category.first()
        category_data = {}

        if product_category:
            category_data['id'] = product_category.id
            category_data['name'] = product_category.name

            product_id = obj.id
            child_categories = Category.objects.filter(parent=product_category, product__id=product_id).distinct()
            category_data['children'] = CategorySerializer(child_categories, many=True).data

        return category_data
    

    def get_xususiyatlari(self, obj):
        xususiyatlari = obj.xususiyatlari.all()
        serializer = XususiyatlariSerializer(xususiyatlari, many=True)
        return serializer.data


    def get_images(self, obj):
        images = obj.imagesd.all()
        serializer = ProductImageSerializer(images, many=True)
        return serializer.data
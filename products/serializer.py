from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product, ProductImage, ProductComment, Category, ImageUpload, Subcategory
from drf_writable_nested import WritableNestedModelSerializer


User = get_user_model()



class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['name', 'slug']



class SubcategorySerializer(serializers.ModelSerializer):
    children = ChildrenSerializer()
    # products = ProductSerializer(many=True)

    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'slug', 'children')



class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)


    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'subcategories', 'created_at']
        # depth = 1



class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = "__all__"



class ProductImageSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    image = ImageUploadSerializer(read_only = False)
    class Meta:
        model = ProductImage
        fields = "__all__"



class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = "__all__"



class ProductSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    category = CategorySerializer(read_only = False)
    product_images = ProductImageSerializer(read_only = False)
    product_comments = ProductCommentSerializer(read_only = False)
    class Meta:
        model = Product
        fields = ['id','category','name','price','total_available','total_count','description','product_images','product_comments','links']

    def get_links(self, obj):
        request = self.context['request']
        links = {
                'self': reverse('product-detail',
                kwargs = {'pk': obj.pk}, request=request),
                # 'business': None,
                }

        # if obj.business:
        #     links['business'] = reverse('business-detail',
        #         kwargs = {'pk': obj.business}, request=request)        
        return links
    


class ProductListByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return Product.objects.filter(category__slug=category_slug)

        
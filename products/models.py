from django.db import models
from django.contrib.auth import get_user_model

from users.models import ImageUpload


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class ProductImage(models.Model):
    image = models.ForeignKey(ImageUpload, related_name="product_image", on_delete=models.CASCADE)
    is_cover = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.image}"



class ProductComment(models.Model):
    user = models.ForeignKey(User, related_name="user_comments_on_product", on_delete=models.CASCADE)
    comment = models.TextField()
    rate = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="product_categories", on_delete=models.CASCADE)
    # business = models.ForeignKey(Business, related_name="belongs_to_business", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    total_available = models.PositiveIntegerField()
    total_count = models.PositiveIntegerField()
    description = models.TextField()
    product_images = models.ForeignKey(ProductImage, related_name="product_images", on_delete=models.CASCADE)
    product_comments = models.ForeignKey(ProductComment, related_name="product_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("-created_at",)



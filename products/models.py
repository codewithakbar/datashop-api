from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from users.models import ImageUpload

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


User = get_user_model()


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)


    class MPTTMeta:
        order_insertion_by = ['name']
 

    def get_full_path(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' / '.join(full_path[::-1])

    def __str__(self):
        return self.get_full_path()

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.slug)])



class ProductComment(models.Model):
    user = models.ForeignKey(User, related_name="user_comments_on_product", on_delete=models.CASCADE)
    comment = models.TextField()
    rate = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(MPTTModel):
    category = models.ManyToManyField(Category)
    # business = models.ForeignKey(Business, related_name="belongs_to_business", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    total_available = models.PositiveIntegerField()
    total_count = models.PositiveIntegerField()
    description = models.TextField()
    
    product_comments = models.ForeignKey(ProductComment, related_name="product_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("-created_at",)

class Xususiyatlari(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='xususiyatlari')

    def __str__(self) -> str:
        return self.title


class Images(models.Model):
    product = models.ForeignKey(Product, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='contents/%Y/%m/%d', blank=True, null=True)
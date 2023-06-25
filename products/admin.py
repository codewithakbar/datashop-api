from django.contrib import admin

from .models import Product, Category, ProductImage, ProductComment, Subcategory

from mptt.admin import DraggableMPTTAdmin

class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    prepopulated_fields = {'slug': ('name',)}



class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryInline]
    prepopulated_fields = {'slug': ('name',)}



class ProductAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('name',)}
    



admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductComment)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory)
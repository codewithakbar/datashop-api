from django.contrib import admin

from .models import Product, Category, Images, ProductComment, Xususiyatlari

from mptt.admin import DraggableMPTTAdmin

from modeltranslation.admin import TranslationAdmin


class XususiyatlariInline(admin.TabularInline):
    model = Xususiyatlari


class ProductImageiInline(admin.TabularInline):
    model = Images


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):

    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',)
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Product)
class ProductAdmin(DraggableMPTTAdmin):
    inlines = [XususiyatlariInline, ProductImageiInline]
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',)
    # prepopulated_fields = {'slug': ('name',)}






admin.site.register(ProductComment)

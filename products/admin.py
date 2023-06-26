from django.contrib import admin

from .models import Product, Category, ProductImage, ProductComment, Subcategory

from mptt.admin import DraggableMPTTAdmin

from modeltranslation.admin import TranslationAdmin


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    prepopulated_fields = {'slug': ('name',)}




class CategoryAdmin(TranslationAdmin):
    inlines = [SubcategoryInline]
    prepopulated_fields = {'slug': ('name',)}

    group_fieldsets = True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    

    list_display = ("name", )
    # prepopulated_fields = {'slug': ('name',)}
    group_fieldsets = True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }




admin.site.register(ProductImage)
admin.site.register(ProductComment)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory)
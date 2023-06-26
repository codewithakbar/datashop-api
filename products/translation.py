from modeltranslation.translator import TranslationOptions, register
from .models import Category, Subcategory, Product

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Subcategory)
class SubcategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

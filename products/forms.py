from django_filters.rest_framework import BooleanFilter, FilterSet, DateFilter
from django.contrib.auth import get_user_model
from .models import Product, Category


class NullFilter(BooleanFilter):
    """ Filter on a field set as null or not."""
    def filter(self, qs, value):
        if value is not None:
            return qs.filter(**{'%s__isnull' % self.name: value})
        return qs


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = ('total_count','price','category')







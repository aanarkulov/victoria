import django_filters

from catalog.models import Product


class ProductFilters(django_filters.FilterSet):
    created = django_filters.CharFilter(method='filter_created')
    action = django_filters.CharFilter(method='filter_action')
    popular = django_filters.CharFilter(method='filter_popular')

    def filter_created(self, queryset, name, value):
        if value:
            return Product.objects.order_by('-created')

    def filter_action(self, queryset, name, value):
        if value:
            return Product.objects.filter(action=True)

    def filter_popular(self, queryset, name, value):
        if value:
            return Product.objects.filter(popular=True)

    class Meta:
        model = Product
        fields = ('type', 'size', 'season', 'created', 'action', 'popular')

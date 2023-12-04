from django_filters import rest_framework as filters

from .models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    status = filters.CharFilter(field_name='status')
    created_at_before = filters.DateFilter(field_name='created_at', lookup_expr='lte')
    created_at_after = filters.DateFilter(field_name='created_at', lookup_expr='gte')

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator']

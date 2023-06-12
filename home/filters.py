from django.contrib.auth.models import User
from home.models import Property
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]

class PropertyFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(lookup_expr='icontains')
    asset_type = django_filters.CharFilter(lookup_expr='icontains')
    tags = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Property
        fields = ['location','asset_type','tags']
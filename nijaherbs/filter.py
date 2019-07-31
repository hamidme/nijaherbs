from django.contrib.auth.models import Herb
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Herb
        fields = ['local_Name', 'english_Name', 'botanical_Name', 'category', ]
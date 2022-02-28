import django_filters
from django_filters import CharFilter
from Boomie.models import *

class TitleFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr="contains")
    class Meta:
        model = Post
        fields = ['title']

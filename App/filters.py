import django_filters
from django_filters import CharFilter
from App.models import *
from django import forms

class TitleFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr="icontains",
        widget = forms.TextInput(attrs = {
            'class': 'search-input',
            'placeholder': 'Enter Your Search ...'
        })
    )
    class Meta:
        model = Post
        fields = ['title']

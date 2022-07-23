import django_filters
from .models import People

class ProductFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending'),
        ('descending'),
    )

    ordering = django_filters.ChoiceFilter(label='Сортировка', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = People
        fields = {
            'name': ['icontains'],
            'age': ['icontains'],
            'master': ['icontains'],
        }

    def filter_by_order(self, queryset, name, value):
        expression = 'created' if value == 'По дате' else '-created'
        return queryset.order_by(expression)
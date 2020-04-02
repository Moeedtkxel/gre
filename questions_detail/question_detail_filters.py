from django_filters import rest_framework as filters
from .models import Questions_detail


class QuestionFilter(filters.FilterSet):
    type_id = filters.CharFilter(lookup_expr='iexact',)

    # Keeping this as an example for foreign key
    # org = filters.NumberFilter(name='organization__id', lookup_expr='exact')
    class Meta:
        model = Questions_detail
        fields = ['type_id']

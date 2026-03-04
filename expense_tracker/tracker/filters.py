import django_filters

from expense_tracker.tracker.models import Record


class RecordFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    date = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(attrs={"placeholder": "DD/MM/YYYY"}),
    )

    class Meta:
        model = Record
        fields = ["name", "date", "amount", "category"]

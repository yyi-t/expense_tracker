from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from expense_tracker.tracker.models import Record


class RecordListView(TemplateView):
    template_name = "tracker/record_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["records"] = []
        if self.request.user.is_authenticated:
            context["records"] = Record.objects.filter(user=self.request.user)
        return context


class RecordDetailView(DetailView):
    model = Record
    template_name = "tracker/record_detail.html"
    context_object_name = "record"

    def get_queryset(self):
        # Get the base queryset
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

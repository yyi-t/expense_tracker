from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from expense_tracker.tracker.filters import RecordFilter
from expense_tracker.tracker.forms import RecordForm
from expense_tracker.tracker.models import Record


class RecordListView(TemplateView):
    template_name = "tracker/record_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        records = Record.objects.none()
        if self.request.user.is_authenticated:
            records = Record.objects.filter(user=self.request.user).order_by(
                "-date",
                "category",
                "name",
            )
        f = RecordFilter(self.request.GET, queryset=records)
        context["RecordFilter"] = f
        context["records"] = f.qs
        return context

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ["tracker/record_list.html"]
        return ["tracker/user_login.html"]


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = "tracker/record_form.html"
    success_url = reverse_lazy("tracker:record-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ["tracker/record_form.html"]
        return ["tracker/user_login.html"]


class RecordDetailView(DetailView):
    model = Record
    template_name = "tracker/record_detail.html"
    context_object_name = "record"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset.filter(user=self.request.user)
        return Record.objects.none()


class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    template_name = "tracker/record_form.html"
    success_url = reverse_lazy("tracker:record-list")

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset.filter(user=self.request.user)
        return Record.objects.none()

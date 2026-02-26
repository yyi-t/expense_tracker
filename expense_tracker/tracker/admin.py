from django.contrib import admin

from expense_tracker.tracker.models import Record
from expense_tracker.tracker.models import RecordCategory

# Register your models here.
admin.site.register(RecordCategory)
admin.site.register(Record)

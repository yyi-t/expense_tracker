from django import forms

from expense_tracker.tracker.models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["date", "name", "description", "amount", "category"]
        widgets = {
            "date": forms.DateInput(
                format="%Y-%m-%d",
                attrs={"type": "date"},
            ),
        }

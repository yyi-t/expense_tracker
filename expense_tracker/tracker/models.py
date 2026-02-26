import datetime

from django.conf import settings
from django.db import models
from django.db.models import CheckConstraint
from django.db.models import Q


class RecordCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, blank=True, default="")
    slug_name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Record Categories"

    def __str__(self):
        return self.name


class Record(models.Model):
    date = models.DateField(default=datetime.date.today)
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, blank=True, default="")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(RecordCategory, on_delete=models.PROTECT)

    class Meta:
        constraints = [
            CheckConstraint(condition=Q(amount__gt=0), name="amount > 0"),
        ]

    def __str__(self):
        return f"{self.date} {self.name} {self.amount}"

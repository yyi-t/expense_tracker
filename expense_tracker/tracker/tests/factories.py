import factory

from expense_tracker.tracker.models import Record
from expense_tracker.tracker.models import RecordCategory
from expense_tracker.users.tests.factories import UserFactory


class RecordCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RecordCategory

    name = factory.Faker("name")


class RecordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Record

    user = factory.SubFactory(UserFactory)
    name = factory.Faker("name")
    category = factory.SubFactory(RecordCategoryFactory)
    amount = factory.Faker(
        "pydecimal",
        min_value=0.05,
        max_value=99999999.99,
        right_digits=2,
        positive=True,
    )

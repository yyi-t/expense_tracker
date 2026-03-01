from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from expense_tracker.tracker.models import Record
from expense_tracker.tracker.models import RecordCategory
from expense_tracker.tracker.tests.factories import RecordFactory
from expense_tracker.users.tests.factories import UserFactory


class RecordViewTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.record_1 = RecordFactory(user=self.user)
        self.record_2 = RecordFactory(user=self.user)
        self.record_3 = RecordFactory()

        self.client.force_authenticate(user=self.user)

    def test_get_record_list(self):
        url = reverse("api:record-list")
        response = self.client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2  # noqa: PLR2004

    def test_post_record(self):
        url = reverse("api:record-list")
        record_category = RecordCategory.objects.first().id
        post_data = {
            "date": "2026-02-15",
            "name": "Pizza",
            "amount": 15.00,
            "category": record_category,
        }
        response = self.client.post(url, post_data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        record = Record.objects.all()
        assert len(record) == 4  # noqa: PLR2004

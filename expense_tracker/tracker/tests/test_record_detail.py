from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from expense_tracker.tracker.models import Record
from expense_tracker.tracker.models import RecordCategory
from expense_tracker.tracker.tests.factories import RecordFactory
from expense_tracker.users.tests.factories import UserFactory


class RecordDetailViewTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.record_1 = RecordFactory(user=self.user)
        self.record_2 = RecordFactory(user=self.user)
        self.record_3 = RecordFactory()

        self.client.force_authenticate(user=self.user)

    def test_get_record_detail(self):
        url = reverse("api:record-detail", args=[self.record_1.id])
        response = self.client.get(url, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 5  # noqa: PLR2004
        expected_data = {
            "date": self.record_1.date.strftime("%Y-%m-%d"),
            "name": self.record_1.name,
            "description": self.record_1.description,
            "amount": str(self.record_1.amount),
            "category_name": self.record_1.category.name,
        }
        assert response.data == expected_data

    def test_delete_record(self):
        record_4 = RecordFactory(user=self.user)
        record = Record.objects.all()
        assert len(record) == 4  # noqa: PLR2004

        url = reverse("api:record-detail", args=[record_4.id])
        response = self.client.delete(url, format="json")

        assert response.status_code == status.HTTP_204_NO_CONTENT
        record = Record.objects.all()
        assert len(record) == 3  # noqa: PLR2004

    def test_patch_record(self):
        patch_data = {
            "date": "2026-01-15",
        }
        url = reverse("api:record-detail", args=[self.record_1.id])
        response = self.client.patch(url, patch_data, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 5  # noqa: PLR2004
        expected_data = {
            "date": "2026-01-15",
            "name": self.record_1.name,
            "description": self.record_1.description,
            "amount": str(self.record_1.amount),
            "category": self.record_1.category.id,
        }
        assert response.data == expected_data

    def test_put_record(self):
        record_category = RecordCategory.objects.first().id
        put_data = {
            "date": "2026-02-15",
            "name": "Pizza",
            "amount": 15.00,
            "category": record_category,
        }
        url = reverse("api:record-detail", args=[self.record_1.id])
        response = self.client.put(url, put_data, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 5  # noqa: PLR2004
        expected_data = {
            "date": "2026-02-15",
            "name": "Pizza",
            "description": self.record_1.description,
            "amount": "15.00",
            "category": record_category,
        }
        assert response.data == expected_data

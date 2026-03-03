from rest_framework import serializers

from expense_tracker.tracker.models import Record


class RecordSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name")

    class Meta:
        model = Record
        fields = ("date", "name", "description", "amount", "category_name")


class RecordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ("date", "name", "description", "amount", "category")


class RecordUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ("date", "name", "description", "amount", "category")

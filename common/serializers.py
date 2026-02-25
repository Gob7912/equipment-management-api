from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Equipment, Assignment


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"

    def validate_name(self, value):
        if len(value) < 3:
            raise ValidationError("Name kamida 3 ta belgidan iborat bo'lishi kerak.")
        return value

    def validate_serial_number(self, value):
        if len(value) < 5:
            raise ValidationError("Serial number juda qisqa.")
        return value


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"

    def validate(self, data):
        if data["equipment"].is_assigned:
            raise ValidationError("Equipment already biriktirilgan.")
        return data
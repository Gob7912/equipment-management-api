from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=100, unique=True)
    is_assigned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=255)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipment.name} -> {self.assigned_to}"
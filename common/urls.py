from django.urls import path
from .views import (
    EquipmentCreateAPIView,
    EquipmentListAPIView,
    EquipmentDetailAPIView,
    EquipmentPutAPIView,
    EquipmentPatchAPIView,
    EquipmentDeleteAPIView,
    AssignmentCreateAPIView
)

urlpatterns = [
    path("equipment/create/", EquipmentCreateAPIView.as_view()),
    path("equipment/", EquipmentListAPIView.as_view()),
    path("equipment/<int:pk>/", EquipmentDetailAPIView.as_view()),
    path("equipment/<int:pk>/put/", EquipmentPutAPIView.as_view()),
    path("equipment/<int:pk>/patch/", EquipmentPatchAPIView.as_view()),
    path("equipment/<int:pk>/delete/", EquipmentDeleteAPIView.as_view()),
    path("assignment/create/", AssignmentCreateAPIView.as_view()),
]
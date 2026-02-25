from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Equipment, Assignment
from .serializers import EquipmentSerializer, AssignmentSerializer


class EquipmentCreateAPIView(APIView):
    def post(self, request):
        serializer = EquipmentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(
            {"message": "CREATED", "id": serializer.data["id"]},
            status=status.HTTP_201_CREATED
        )


class EquipmentListAPIView(APIView):
    def get(self, request):
        equipments = Equipment.objects.all()

        fr = request.query_params.get("filter")
        search = request.query_params.get("q")

        if fr:
            if fr.lower() == "assigned":
                equipments = equipments.filter(is_assigned=True)
            elif fr.lower() == "available":
                equipments = equipments.filter(is_assigned=False)

        if search:
            equipments = equipments.filter(name__icontains=search)

        
        equipments = equipments.values("name", "is_assigned")
        return Response(list(equipments), status=status.HTTP_200_OK)


class EquipmentDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            equipment = Equipment.objects.get(pk=pk)
        except Equipment.DoesNotExist:
            return Response(
                {"error": "Topilmadi"},
                status=status.HTTP_404_NOT_FOUND
            )

        data = EquipmentSerializer(equipment).data
        return Response(data, status=status.HTTP_200_OK)


class EquipmentPutAPIView(APIView):
    def put(self, request, pk):
        try:
            equipment = Equipment.objects.get(pk=pk)
        except Equipment.DoesNotExist:
            return Response(
                {"error": "Topilmadi"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EquipmentSerializer(equipment, data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(
            {"message": "yangilandi", "Yangi versiyasi": serializer.data},
            status=status.HTTP_200_OK
        )


class EquipmentPatchAPIView(APIView):
    def patch(self, request, pk):
        if not request.data:
            return Response(
                {"error": "Kamida bitta fieldni yangilang"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            equipment = Equipment.objects.get(pk=pk)
        except Equipment.DoesNotExist:
            return Response(
                {"error": "Topilmadi"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EquipmentSerializer(
            equipment,
            data=request.data,
            partial=True
        )

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(
            {"message": "yangilandi", "Yangi versiyasi": serializer.data},
            status=status.HTTP_200_OK
        )


class EquipmentDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            equipment = Equipment.objects.get(pk=pk)
        except Equipment.DoesNotExist:
            return Response(
                {"error": "Topilmadi"},
                status=status.HTTP_404_NOT_FOUND
            )

        equipment.delete()

        return Response(
            {"message": "O'chirildi"},
            status=status.HTTP_204_NO_CONTENT
        )


class AssignmentCreateAPIView(APIView):
    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        assignment = serializer.save()

        equipment = assignment.equipment
        equipment.is_assigned = True
        equipment.save()

        return Response(
            {"message": "Equipment biriktirildi"},
            status=status.HTTP_201_CREATED
        )
from rest_framework import viewsets, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from missions.models import Mission
from missions.serializers import (
    MissionSerializer,
    MissionUpdateSerializer,
    AssignCatToMissionSerializer
)


class MissionViewSet(ModelViewSet):
    queryset = Mission.objects.select_related("cat").prefetch_related("targets")
    serializer_class = MissionSerializer

    def get_serializer_class(self):
        if self.action in ('update', 'partial_update'):
            return MissionUpdateSerializer
        elif self.action == 'assign_cat':
            return AssignCatToMissionSerializer
        return self.serializer_class

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()

        if mission.cat:
            raise ValidationError("Cannot delete this mission because cat was assigned.")

        mission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        methods=["POST"],
        detail=True,
        url_path="assign-cat"
    )
    def assign_cat(self, request, pk=None):
        """Endpoint for assigning cat to specific mission"""
        mission = self.get_object()
        serializer = self.get_serializer(mission, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

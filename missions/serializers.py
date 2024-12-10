from django.db import transaction
from rest_framework import serializers

from missions.models import Target, Mission


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ('id', 'name', 'country', 'notes', 'is_completed')


class TargetUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Target
        fields = ('id', 'notes', 'is_completed')


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True, read_only=False, allow_empty=False)

    class Meta:
        model = Mission
        fields = ('id', 'cat', 'is_completed', 'targets')

    def create(self, validated_data):
        with transaction.atomic():
            targets = validated_data.pop('targets')
            mission = Mission.objects.create(**validated_data)

            target_names = [target['name'] for target in targets]
            if len(target_names) != len(set(target_names)):
                raise serializers.ValidationError("Each target must have a unique name for mission.")

            for target in targets:
                Target.objects.create(mission=mission, **target)
            return mission


class MissionUpdateSerializer(serializers.ModelSerializer):
    targets = TargetUpdateSerializer(many=True)

    class Meta:
        model = Mission
        fields = ('id', 'is_completed', 'targets')

    def update(self, instance, validated_data):
        targets = validated_data.pop('targets')

        for target in targets:
            try:
                target_instance = Target.objects.get(id=target.get('id'))
            except Target.DoesNotExist:
                raise serializers.ValidationError('Target with specified id does not exist.')

            if target_instance.notes != target.get('notes') and (target_instance.is_completed or instance.is_completed):
                raise serializers.ValidationError("Cannot update 'notes' because the target or mission is completed.")

            target_instance.is_completed = target.get('is_completed', target_instance.is_completed)
            target_instance.notes = target.get('notes', target_instance.notes)
            target_instance.save()

        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.save()

        return instance


class AssignCatToMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ('id', 'cat')

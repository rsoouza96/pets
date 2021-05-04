from rest_framework import serializers


class CharacteristicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    characteristic = serializers.CharField()


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    scientific_name = serializers.CharField()


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    characteristic_set = CharacteristicSerializer(many=True)
    group = GroupSerializer()
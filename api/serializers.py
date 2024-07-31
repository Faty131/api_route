from rest_framework import serializers

class PointSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)  # Champ optionnel
    designation = serializers.CharField(max_length=100, required=False)  # Champ optionnel
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6)

class StartPositionSerializer(serializers.Serializer):
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6)

class CalculateRouteSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    startPosition = StartPositionSerializer()
    parameters = serializers.DictField()
    points = PointSerializer(many=True)
    averageSpeed = serializers.DecimalField(max_digits=5, decimal_places=2, required=True)

class GenerateMapUrlSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    path = PointSerializer(many=True)

from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

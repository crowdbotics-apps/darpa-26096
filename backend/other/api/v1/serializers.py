from rest_framework import serializers
from other.models import Foreign_Asset1, Foreign_Asset2


class Foreign_Asset1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Foreign_Asset1
        fields = "__all__"


class Foreign_Asset2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Foreign_Asset2
        fields = "__all__"

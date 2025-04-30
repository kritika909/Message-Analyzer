from .models import QueryLog
from rest_framework import serializers

class RequestSerializer(serializers.Serializer):
    query = serializers.CharField()

class ResponseSerializer(serializers.Serializer):
    query = serializers.CharField()
    analysis = serializers.DictField()
    suggestion = serializers.ListField()

class QuerySerializer(serializers.Serializer):
    class Meta:
        model = QueryLog
        fields = '__all__'

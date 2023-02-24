from rest_framework import serializers

from resources.models import Transfer


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = "__all__"


class TransferMeSerializer(serializers.ModelSerializer):
    origin = serializers.SerializerMethodField()
    destiny = serializers.SerializerMethodField()

    class Meta:
        model = Transfer
        fields = ('id', 'value', 'description', 'public', 'created_at', 'origin', 'destiny')

    def get_origin(self, obj):
        return obj.origin.user.full_name
    
    def get_destiny(self, obj):
        return obj.destiny.user.full_name

from rest_framework import serializers

from app.domain.models.deposit import Deposit


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = "__all__"

    def create(self, validated_data):
        return Deposit(**validated_data)
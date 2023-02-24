from rest_framework import serializers

from resources.models.models_account import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'balance',)

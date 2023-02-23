from rest_framework import serializers

from resources.models.models_user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'full_name', 'birthdate', 'phone', 'cpf',)

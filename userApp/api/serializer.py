from rest_framework import serializers
from userApp.models import Account
from rest_framework.validators import UniqueValidator


class SerializerUser(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=128, write_only=True)
    email = serializers.CharField(max_length=100,
                                  validators=[UniqueValidator(queryset=Account.objects.all())])

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name']
        # Devuelve las propiedades
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('Contraseñas diferentes')

        return attrs

    def create(self, validated_data):
        del validated_data['password2']

        account = Account.objects.create_user(
            **validated_data
        )

        account.set_password(validated_data.get('password'))

        return account


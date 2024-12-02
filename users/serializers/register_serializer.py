from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    phone_number = serializers.CharField(help_text="Номер телефона пользователя")
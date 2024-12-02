from rest_framework import serializers

class VerifyCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(help_text="Номер телефона пользователя")
    verification_code = serializers.CharField(help_text="Код подтверждения")
import time
import random

from drf_spectacular.utils import extend_schema

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.cache import cache
from users.models import User
from users.serializers.register_serializer import RegisterSerializer

@extend_schema(
    summary="Зарегестрировать номер телефона",
    description="Регестрирует номер телефона и отправляет SMS с кодом для подтвердждения регистрации",
    responses={200: "Verification code sent"}
)
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']

            verification_code = ''.join(random.choices('0123456789', k=4))
            cache.set(f'verify_code_{phone_number}', verification_code, timeout=300)
            time.sleep(2)  # Имитация отправки кода
            print(f'Code for phone number {phone_number}: {verification_code}')

            user = User.objects.get_or_create(phone_number=phone_number)[0]
            user.save()

            return Response({'message': 'Verification code sent'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

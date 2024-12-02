from drf_spectacular.utils import extend_schema

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.core.cache import cache

from users.serializers.verify_code_serializer import VerifyCodeSerializer
from users.models import User

def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {'access': str(refresh.access_token)},

@extend_schema(
    summary="Подтвердить регистрацию номера телефона",
    description="Подтверждает номер телефона по коду пришедшему в SMS",
    responses={200: "User authenticated",
               400: "Invalid code"}
)
class VerifyCodeView(APIView):
    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)

        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']

            verification_code = serializer.validated_data['verification_code']
            cached_code = cache.get(f'verify_code_{phone_number}')

            if cached_code and cached_code == verification_code:
                user, created = User.objects.get_or_create(phone_number=phone_number)
                token = get_token_for_user(user)

                return Response({
                    'message': 'User authenticated',
                    'new_user': created,
                    'token': token,
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid code'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

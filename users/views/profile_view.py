from drf_spectacular.utils import extend_schema_view, extend_schema

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from users.serializers.profile_serializer import ProfileSerializer
from users.models import User

@extend_schema_view(
    get=extend_schema(
        summary="Получить профиль пользователя",
        description="Возвращает данные профиля текущего пользователя, включая список рефералов.",
        responses={200: "Список данных получен."}
    ),
    post=extend_schema(
        summary="Активация инвайт-кода у пользователя",
        description="Активирует инвайт-код для текущего пользователя",
        responses={201: "Инвайт-код успешно активирован.",
                   400: "Bad request"
        },
    ),
)
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(f"Authorization Header: {request.headers.get('Authorization')}")
        print(f"Authenticated User: {request.user}")
        print(f"User ID from Token: {getattr(request.user, 'id', None)}")

        user_id = request.user.id
        user = get_object_or_404(User, id=user_id)
        print("USER: ", user)

        serializer = ProfileSerializer(instance=user)

        return Response(serializer.data)

    def post(self, request):
        user = request.user
        invite_code = request.data.get('invite_code')

        if not invite_code:
            return Response({'error': 'Invite code is required'}, status=status.HTTP_400_BAD_REQUEST)

        if user.activated_invite_code:
            return Response({'error': 'Invite code already used'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            inviter = User.objects.get(invite_code=invite_code)
            user.activated_invite_code = inviter.invite_code
            user.save()

            return Response({'message': 'Invite code applied'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Invalid invite code'}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import serializers

from users.models import User

class ProfileSerializer(serializers.ModelSerializer):

    referred_users = serializers.SerializerMethodField(help_text="Пользователи которые активировали инвайт-код текущего пользователя")

    class Meta:
        model = User
        fields = ['phone_number', 'invite_code', 'activated_invite_code', 'referred_users']
        extra_kwargs = {
            'phone': {'help_text': 'Номер телефона пользователя'},
            'invite_code': {'help_text': 'Уникальный инвайт-код пользователя'},
            'activated_invite_code': {'help_text': 'Инвайт-код который активировал пользователь'},
        }

    def get_referred_users(self, obj):
        return User.objects.filter(activated_invite_code=obj.invite_code).values_list('phone_number', flat=True)

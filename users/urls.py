from django.urls import path
from users.views.register_view import RegisterView
from users.views.verify_code_view import VerifyCodeView
from users.views.profile_view import ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('verify/', VerifyCodeView.as_view()),
    path('profile/', ProfileView.as_view()),
]
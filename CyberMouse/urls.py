from django.urls import path
from .views import LoginView, SignupView, ResetPasswordView, MailVerificationView, HomeView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('reset-password/', ResetPasswordView.as_view(), name='resetPassword'),
    path('email-verification/', MailVerificationView.as_view(), name='emailVerification'),
    path('home', HomeView.as_view(), name='home'),
]

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
class LoginView(View):

    def login_view(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Connexion reussite")
        else:
            return HttpResponse("ECHEC DE CO  ! ")
    def get(self, request):
        return render(request, 'login.html')
"""
    def post(self, request):
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            
            user = authenticate(request, username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message.succes(request, f'Bienvenue, {username} !)
                    return redirect('home')
                else: 
                    message.error(request, "compte pas encore active")
            else:
                Nom ou id invalide
        return render(request,'login.html', {'form': form})
        
        
"""


class SignupView(View):
    def get(self, request):
        # form = UserRegistrationForm()
        return render(request, 'signup.html')
    """
        def post(self, request):
            form = UserResistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.activation_token = uuid.uuid4()
                user.save()
                self.sendVerificationMail(user)
                messages.success(request, 
                    'Blalaba t'as réussi' Verifie ton mail pour activer le compte.')
                return redirect('home')
            return render(request, 'signup.html', {'form': form})

        def sendVerificationMail(self,user):
            subkect = 'Verif Adresse mail'
            message = f'Cliquez sur le lien suivant pour vérifier votre adresse e-mail : {settings.SITE_URL}/verify-email/{user.activation_token}/'
            from_email = settings.DEFAULT
            recipient_list = [user.email]
            send_mail(subject, message, from_mail, recipient_list
    """
class HomeView(TemplateView):
    template_name = 'home.html'

class LevelOneView(View):
    def get(self, request):
        return render(request, 'levelOne.html')

class ResetPasswordView(View):
    def get(self, request):
        return render(request, 'resetPassword.html')

    """
        def post(self, request):
            email = request.POST.get('email')
            user = User.objects.filter(email=email).first()
            if user:
                reset_token = uuid.uuid4()
                user.reset_token = reset_token
                user.save()
                self.sendResetMail(user)
                messages.success(request, 'Un lien de réinitialisation de mot de passe a été envoyé à votre e-mail.')
                return redirect('login')
            else:
                messages.error(request, 'Aucun utilisateur associé à cet e-mail.')
            return render(request, 'resetPassword.html')

        def sendResetMail(self, user):
            subject = 'Réinitialisation de votre mot de passe'
            message = f'Cliquez sur le lien suivant pour réinitialiser votre mot de passe : {settings.SITE_URL}/reset-password/{user.reset_token}/'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)
    """

class MailVerificationView(View):
    def get(self, request):
        return render(request, 'emailverification.html')

    """
        def post(self, request):
            token = request.GET.get('token')
            user = User.objects.filter(activation_token=token).first()
            if user:
                user.is_active = True
                user.activation_token = None
                user.save()
                messages.success(request, 'Votre compte a été vérifié avec succès. Vous pouvez maintenant vous connecter.')
                return redirect('login')
            else:
                messages.error(request, 'Lien de vérification invalide ou expiré.')
            return render(request, 'emailverification.html')
    """

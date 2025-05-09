from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuariosCriarForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-mail")
    nome_completo = forms.CharField(required=True, label="Nome completo")
    foto = forms.ImageField(required=False, label="Foto de perfil")
    bio = forms.CharField(widget=forms.Textarea, required=False, label="Biografia")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nome_completo', 'foto', 'bio']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            Usuario.objects.create(
                user=user,
                nome_completo=self.cleaned_data['nome_completo'],
                imagem=self.cleaned_data.get('foto'),
                bio=self.cleaned_data.get('bio')
            )
        return user
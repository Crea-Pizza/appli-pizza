from dateutil.relativedelta import relativedelta
from django import forms
from django.forms import widgets
from django.forms.utils import ErrorList

from django.utils.translation import ugettext_lazy as _


class RegisterForm(forms.Form):
    # Informations utilisateur
    a = _("Votre prénom")
    first_name = forms.CharField(
        label=a,
        localize=True,
        required=True,
        widget=widgets.TextInput(attrs={
            'title': a,
            'placeholder': a,
            'class': 'form-control'
        })
    )

    a = _("Votre nom")
    last_name = forms.CharField(
        label=a,
        localize=True,
        required=True,
        widget=widgets.TextInput(attrs={
            'title': a,
            'placeholder': a,
            'class': 'form-control'
        })
    )

    a = _("Votre pseudo")
    username = forms.CharField(
        label=a,
        localize=True,
        required=True,
        widget=widgets.TextInput(attrs={
            'title': a,
            'placeholder': a,
            'class': 'form-control'
        })
    )

    a = _("Votre email")
    email = forms.CharField(
        label=a,
        localize=True,
        required=True,
        widget=widgets.TextInput(attrs={
            'title': a,
            'placeholder': a,
            'class': 'form-control'
        })
    )

    a = _("Votre mot de passe")
    password = forms.CharField(
        label=a,
        localize=True,
        required=True,
        widget=widgets.TextInput(attrs={
            'title': a,
            'placeholder': a,
            'class': 'form-control',
            'type': "password"
        })
    )

    a = _("Confirmez le mot de passe")
    password_verif = forms.CharField(
        label=a,
        localize=True,
        required=True,
        widget=widgets.TextInput(attrs={
            'title': a,
            'placeholder': a,
            'class': 'form-control',
            'type': "password"
        })
    )

    # Information personne
    a = _("Adresse")
    adresse = forms.CharField(
        label=a,
        localize=True,
        required=True,
        widget=widgets.TextInput(attrs={
            'title': a,
            'placeholder': a,
            'class': 'form-control'
        })
    )

    a = _("Code postal")
    cp = forms.IntegerField(
        label=a,
        localize=True,
        required=True,
        widget=widgets.NumberInput(attrs={
            'title': a,
            'placeholder': a,
            'class': 'form-control'
        })
    )

    a = _("Ville")
    ville = forms.CharField(
        label=a,
        localize=True,
        required=True,
        widget=widgets.TextInput(attrs={
            'title': a,
            'placeholder': a,
            'class': 'form-control'
        })
    )

    a = _("Téléphone")
    telephone = forms.IntegerField(
        label=a,
        localize=True,
        required=True,
        widget=widgets.NumberInput(attrs={
            'title': a,
            'placeholder': a,
            'class': 'form-control'
        })
    )

    def clean_username(self):
        valeur = self.cleaned_data['username']
        if not valeur:
            self.add_error(
                'username',
                "Pas de pseudo"
            )
        return valeur

    def clean(self, valeur=None):
        password = self.cleaned_data['password']
        password_verif = self.cleaned_data['password_verif']
        if password != password_verif:
            self.add_error('password', "Les mots de passe ne sont pas les mêmes.")
        return super(RegisterForm, self).clean()

    def clean_email(self):
        valeur = self.cleaned_data['email']
        return valeur

        # def clean(self):
        # pass

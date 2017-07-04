from django.contrib import auth
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db import IntegrityError
from django.views import generic

from app.form.register import RegisterForm
from app.models.personne import Personne


class RegisterView(generic.FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        retour = super(RegisterView, self).form_valid(form)

        try:
            u = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password'])

        except IntegrityError:
            form.add_error('username',
                           "Ce nom d'utilisateur est déjà utilisé. Merci d'en choisir un autre.")
            return super(RegisterView, self).form_invalid(form)

        Personne.objects.create(user=u,
                                prenom=form.cleaned_data['first_name'],
                                nom=form.cleaned_data['last_name'],
                                mail=form.cleaned_data['email'],
                                adresse1=form.cleaned_data['adresse'],
                                cp=form.cleaned_data['cp'],
                                ville=form.cleaned_data['ville'],
                                telephone=form.cleaned_data['telephone'])

        u.is_active = True
        u.save()

        auth.login(self.request, u)

        # EmailMessage(
        #     subject='Merci !',
        #     body='{}\n'.format("Merci de vous êtes enregistré"),
        #     from_email='test@test.com',
        #     to=['nadege.sery33@gmail.com'],
        #     bcc=['nadege.sery33@gmail.com']).send()

        return retour

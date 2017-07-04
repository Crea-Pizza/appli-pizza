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
                form.cleaned_data['password'],)
            u.last_name = form.cleaned_data['last_name']
            u.first_name = form.cleaned_data['first_name']

            u.is_active = True
            u.save()

            p = Personne.objects.create(user=u)
            p.save()

            auth.login(self.request, u)

        except IntegrityError:
            form.add_error('username',
                           "Ce nom d\'utilisateur est utilisé. Merci d'en choisir un autre.")
            return super(RegisterView, self).form_valid(form)



        EmailMessage(
            subject='Merci !',
            body='{}\n{}\n{}\n'.format("Merci de vous êtes enregistré"),
            from_email='test@test.com',
            to=['nadege.sery33@gmail.com'],
            bcc=['nadege.sery33@gmail.com']).send()

        return retour
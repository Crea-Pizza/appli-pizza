from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import ugettext_lazy as _


from pizzeria import settings


@method_decorator(csrf_exempt, name='dispatch')
class JsonLoginView(generic.View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return JsonResponse({}),
        else:
             return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


       # return JsonResponse({})

    def post(self, request, *args, **kwargs):
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            return HttpResponseForbidden()
        user = authenticate(username=username,
                            password=password)
        if user is not None:
            auth.login(request, user)
            return JsonResponse({
                'message': _('Connecté'),
                'success': True,
            })
        else:
            return JsonResponse({
            'message': _('Erreur de connexion'),
            'success': False,
        })



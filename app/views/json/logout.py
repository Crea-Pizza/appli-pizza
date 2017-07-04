from django.contrib.auth import logout
from django.http import JsonResponse
from django.views import generic
from django.utils.translation import ugettext_lazy as _


class JsonLogout(generic.View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return JsonResponse({
            'message': _('Deconnecté'),
            'success': True,
        })

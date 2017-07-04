from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import ugettext_lazy as _

from app.models.personne import Personne


class JsonIsConnectedView(generic.View):
    def get(self, request):
        if request.user.is_authenticated():
            return JsonResponse({
                'message': _('User connecté'),
                'success': True
            })
        else:
            return JsonResponse({
                'message': _('User non connecté'),
                'success': False
            })

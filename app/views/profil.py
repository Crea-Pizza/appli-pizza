from django.shortcuts import render
from django.views import generic


class ProfilView(generic.TemplateView):
    def voir_profil(request):
        args = {'user': request.user}
        return render(request, '')
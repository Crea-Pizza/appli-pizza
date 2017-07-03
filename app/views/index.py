from django.views import generic

from app.models.ingredient import Ingredient
from app.models.pizza import Pizza


class IndexView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        retour = super(IndexView, self).get_context_data(**kwargs)
        try:
            pizzas_classique = Pizza.objects.filter(categorie=1)
            pizzas_creme = Pizza.objects.filter(categorie=2)

        except Pizza.DoesNotExist:
            pizzas = None
            pizzas_creme = None

        retour["pizzas_classique"] = pizzas_classique
        retour["pizzas_creme"] = pizzas_creme

        return retour

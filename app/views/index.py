from django.views import generic

from app.models.ingredient import Ingredient
from app.models.produit import Produit


class IndexView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        retour = super(IndexView, self).get_context_data(**kwargs)
        try:
            pizzas_classique = Produit.objects.filter(categorie=1)
            pizzas_creme = Produit.objects.filter(categorie=2)
            desserts = Produit.objects.filter(categorie=3)
            boissons = Produit.objects.filter(categorie=4)

        except Produit.DoesNotExist:
            pizzas_classique = None
            pizzas_creme = None
            desserts = None
            boissons = None

        retour["pizzas_classique"] = pizzas_classique
        retour["pizzas_creme"] = pizzas_creme
        retour["desserts"] = desserts
        retour["boissons"] = boissons

        return retour

from django.db import models

from app.models.categorie import Categorie
from app.models.ingredient import Ingredient


class Produit(models.Model):
    ingredients = models.ManyToManyField(Ingredient,
                                         blank=True)
    categorie = models.ForeignKey(Categorie,
                                  null=True,
                                  default=None,
                                  blank=True)
    label = models.CharField(max_length=200,
                             null=True,
                             blank=True,
                             default=None)
    taille = models.CharField(max_length=100,
                              null=True,
                              blank=True,
                              default=None)
    prix = models.FloatField(default=0.0,
                             blank=True,
                             null=True)

    def get_ingredients(self):
        return Ingredient.objects.filter(produit=self)

    def __str__(self):
        return "{} - {} : {} €".format(self.label, self.taille, self.prix)

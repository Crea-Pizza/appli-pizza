from django.db import models

from app.models.produit import Produit


class Commande  (models.Model):
    produit = models.ForeignKey(Produit)
    panier = models.ForeignKey('Panier')
    quantite = models.IntegerField()

    def __str__(self):
        return "{} - {} x {}".format(self.panier, self.produit, self.quantite)

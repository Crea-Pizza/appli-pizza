from django.db import models

from app.models.pizza import Pizza


class Commande  (models.Model):
    pizza = models.ForeignKey(Pizza)
    panier = models.ForeignKey('Panier')
    quantite = models.IntegerField()

    def __str__(self):
        return "{} - {} x {}".format(self.panier, self.pizza, self.quantite)

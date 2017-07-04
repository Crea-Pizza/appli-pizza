from django.contrib.auth.models import User
from django.db import models

from app.models.commande import Commande
from app.models.pizza import Pizza


class Panier(models.Model):
    user = models.ForeignKey(User)
    # Valeur à true signifie que le user n'est pas encore passé par le processus de commande
    active = models.BooleanField(default=True)
    date_creation = models.DateField(null=True)
    id_paiement = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "{}".format(self.user)

    """ Ajoute au panier du client la pizza demandée, ou incrémente sa quantité si elle existe déjà dans le panier """

    def ajouter_au_panier(self, pizza_id):
        pizza = Pizza.objects.get(id=pizza_id)
        # Si la pizza existe dans le panier, on incrémente sa quantité
        try:
            order_exist = Commande.objects.get(pizza=pizza, panier=self)
            order_exist.quantite += 1
            order_exist.save()
        # Si elle n'existe pas, on la rajoute au panier avec la quantité 1
        except Commande.DoesNotExist:
            nouvelle_commande = Commande.objects.create(
                pizza=pizza,
                panier=self,
                quantite=1
            )
            nouvelle_commande.save()

    """ Supprime du panier la pizza ou décrémente sa quantité si elle est supérieure à 1 """

    def supprimer_du_panier(self, pizza_id):
        pizza = Pizza.objects.get(id=pizza_id)
        # Si la pizza existe bien dans le panier
        try:
            order_exist = Commande.objects.get(pizza=pizza, panier=self)
            # On vérifie la quantité. Si elle est supérieure à 1, on en retire une
            if order_exist.quantite > 1:
                order_exist.quantite -= 1
                order_exist.save()
            # Si elle est égale à 1, on la supprime du panier
            else:
                order_exist.delete()
        except Commande.DoesNotExist:
            pass

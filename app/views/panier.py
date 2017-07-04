from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.views import generic

from app.models.commande import Commande
from app.models.panier import Panier
from app.models.pizza import Pizza


class PanierView(generic.TemplateView):

    def ajouter_au_panier(request, pizza_id):
        # L'utilisateur doit être connecté
        if request.user.is_authenticated():
            try:
                # On regarde si le pizza_id passé existe bien parmi les Pizzas
                pizza = Pizza.objects.get(id=pizza_id)
            except ObjectDoesNotExist:
                pass
            else:
                try:
                    # On regarde si un panier existe pour cet utilisateur
                    panier = Panier.objects.get(user=request.user, active=True)
                except ObjectDoesNotExist:
                    # Si il n'en a pas, on lui crée un panier
                    panier = Panier.objects.create(
                        user=request.user
                    )
                    panier.save()
                # On ajoute la pizza au panier
                panier.ajouter_au_panier(pizza_id)
            return redirect('panier')
        else:
            return redirect('/')


    def supprimer_du_panier(request, pizza_id):
        # L'utilisateur doit être connecté
        if request.user.is_authenticated():
            try:
                # On regarde si le pizza_id passé existe bien parmi les Pizzas
                pizza = Pizza.objects.get(id=pizza_id)
            except ObjectDoesNotExist:
                pass
            else:
                # On supprime la pizza demandée du panier
                panier = Panier.objects.get(user=request.user, active=True)
                panier.supprimer_du_panier(pizza_id)
            return redirect('panier')
        else:
            return redirect('/')

    def panier(request):
        if request.user.is_authenticated():
            # Récupération du panier et de toutes les commandes contenues dans ce panier
            panier = Panier.objects.filter(user=request.user.id, active=True)
            commandes = Commande.objects.filter(panier=panier)
            # Total prix
            total = 0
            # Nombre de pizzas
            cpt = 0
            for commande in commandes:
                total += (commande.pizza.prix * commande.quantite)
                cpt += commande.quantite
            context = {
                'panier': commandes,
                'total': total,
                'cpt': cpt,
            }
            return render(request, 'panier.html', context)
        else:
            return redirect('/')
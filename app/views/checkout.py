import paypalrestsdk
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from app.models.commande import Commande
from app.models.panier import Panier


def checkout_paypal(request, panier, commandes):
    # L'utilisateur doit être connecté
    if request.user.is_authenticated():
        items = []
        total = 0
        for commande in commandes:
            total += (commande.produit.prix * commande.quantite)
            produit = commande.produit
            # Préparation de chaque items de la commande
            item = {
                'name': str(produit.label),
                'sku': produit.id,
                'price': str(produit.prix),
                'currency': 'EUR',
                'quantity': commande.quantite
            }
            items.append(item)

        paypalrestsdk.configure({
            "mode": "sandbox",
            "client_id": "ATtl-pRhPILV2id6Kao07pVwkfe8Q9OhoAGHgNOGrfmMUFzrUbl8yXiG-xPC8H9nVnlVRs6rP3eGqo3z",
            "client_secret": "EApOzEBv9p_1GlcvHdccS9zaiUoTRAkK1_Ns6S7nDRgt4fkRRI5JGfHtEkWOR8ORLlYUz2oX-p_-GZQa"
        })

        # Paiement paypal
        paiement = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"},
            "redirect_urls": {
                "return_url": "http://127.0.0.1:8000/process/paypal",
                "cancel_url": "http://127.0.0.1:8000"},
            "transactions": [{
                "item_list": {
                    "items": items},
                "amount": {
                    "total": str(total),
                    "currency": "EUR"},
                "description": "Commande pizzas"}]})

        if paiement.create():
            panier_instance = panier.get()
            panier_instance.id_paiement = paiement.id
            panier_instance.save()

            for lien in paiement.links:
                if lien.method == "REDIRECT":
                    redirect_url = str(lien.href)
                    return redirect_url
        else:
            return reverse('erreur_commande')
    else:
        return redirect('/')


class CheckoutView(generic.TemplateView):
    """ Redirige vers le processus de paiement demandé """

    def checkout(request, processor):
        if request.user.is_authenticated():
            panier = Panier.objects.filter(user=request.user.id, active=True)
            commandes = Commande.objects.filter(panier=panier)
            if processor == "paypal":
                redirect_url = checkout_paypal(request, panier, commandes)
                return redirect(redirect_url)
        else:
            return redirect('/')

    def erreur_commande(request):
        if request.user.is_authenticated():
            return render(request, 'commande/erreur_commande.html')
        else:
            return redirect('/')

    def process_commande(request, processor):
        if request.user.is_authenticated():
            if processor == "paypal":
                id_paiement = request.GET.get('paymentId')
                panier = Panier.objects.filter(id_paiement=id_paiement)
                commandes = Commande.objects.filter(panier=panier)
                total = 0
                for commande in commandes:
                    total += (commande.produit.prix * commande.quantite)
                context = {
                    'panier': commandes,
                    'total': total
                }
                return render(request, 'commande/process_commande.html', context)
        else:
            return redirect('/')

    def complete_commande(request, processor):
        if request.user.is_authenticated():
            panier = Panier.objects.get(user=request.user.id, active=True)
            if processor == 'paypal':
                # Récupération du paiement selon le panier
                paiement = paypalrestsdk.Payment.find(panier.id_paiement)
                # Execution du paiement
                if paiement.execute({"payer_id": paiement.payer.payer_info.payer_id}):
                    message = "Succès ! Votre commande a bien été prise en compte. Id Paiement: %s" % (paiement.id)
                    # Le panier a été commandé, donc il ne sera plus affiché pour le client
                    panier.active = False
                    # Date à laquelle la commande a été effectuée
                    panier.date_creation = timezone.now()
                    panier.save()
                else:
                    message = "Un problème est survenu lors de la transaction. Erreur: %s" % (paiement.error.message)
                context = {
                    'message': message,
                }
                return render(request, 'commande/commande_accomplie.html', context)
        else:
            return redirect('/')

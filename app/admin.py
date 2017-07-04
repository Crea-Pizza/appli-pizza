from django.contrib import admin

from app.models.categorie import Categorie
from app.models.commande import Commande
from app.models.ingredient import Ingredient
from app.models.panier import Panier
from app.models.personne import Personne
from app.models.produit import Produit


class produitAdmin(admin.ModelAdmin):
    list_display = ('label', 'taille', 'prix', 'categorie')


class PanierAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_creation')


class CommandeAdmin(admin.ModelAdmin):
    list_display = ('produit', 'quantite')

admin.site.register(Personne)
admin.site.register(Produit, produitAdmin)
admin.site.register(Ingredient)
admin.site.register(Categorie)
admin.site.register(Panier,PanierAdmin)
admin.site.register(Commande, CommandeAdmin)
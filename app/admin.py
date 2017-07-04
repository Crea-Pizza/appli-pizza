from django.contrib import admin

from app.models.categorie import Categorie
from app.models.commande import Commande
from app.models.ingredient import Ingredient
from app.models.panier import Panier
from app.models.personne import Personne
from app.models.pizza import Pizza

admin.site.register(Personne)
admin.site.register(Pizza)
admin.site.register(Ingredient)
admin.site.register(Categorie)
admin.site.register(Panier)
admin.site.register(Commande)
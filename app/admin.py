from django.contrib import admin

from app.models.categorie import Categorie
from app.models.ingredient import Ingredient
from app.models.pizza import Pizza

admin.site.register(Pizza)
admin.site.register(Ingredient)
admin.site.register(Categorie)
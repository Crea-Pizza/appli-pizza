"""pizzeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app.views.checkout import CheckoutView
from app.views.index import IndexView

from app.views.json.connected import JsonIsConnectedView
from app.views.json.login import JsonLoginView
from app.views.json.logout import JsonLogout
from app.views.panier import PanierView
from app.views.register import RegisterView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='app_index'),
    # CONNEXION / DECONNEXION / INSCRIPTION
    url(r'^login/$', JsonLoginView.as_view(), name='app_json_login'),
    url(r'^logout/$', JsonLogout.as_view(), name='app_json_logout'),
    url(r'^json/connected/$', JsonIsConnectedView.as_view(), name='app_connected'),
    url(r'^register/$', RegisterView.as_view(), name='app_register'),
    # PANIER -- (\d+) : digit
    url(r'^ajouter/(\d+)', PanierView.ajouter_au_panier, name='ajouter_au_panier'),
    url(r'^supprimer/(\d+)', PanierView.supprimer_du_panier, name='supprimer_du_panier'),
    url(r'^commande/panier/', PanierView.panier, name='panier'),
    # COMMANDE -- (\w+) : alpa
    url(r'^checkout/(\w+)', CheckoutView.checkout, name='checkout'),
    url(r'^process/(\w+)', CheckoutView.process_commande, name='process_commande'),
    url(r'^commande/erreur_commande/', CheckoutView.erreur_commande, name='erreur_commande'),
    url(r'^commande/complete_commande/(\w+)', CheckoutView.complete_commande, name='complete_commande'),
]

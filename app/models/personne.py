from django.conf.urls.static import static
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy


class Personne(models.Model):
    user = models.OneToOneField(User)
    prenom = models.CharField(max_length=20, default=None, blank=True)
    nom = models.CharField(max_length=15, default=None, blank=True)
    mail = models.EmailField(max_length=50, default=None, blank=True)
    adresse1 = models.CharField(max_length=40, default=None, blank=True)
    adresse2 = models.CharField(max_length=40, default=None, blank=True)
    cp = models.CharField(max_length=5, default=None, blank=True)
    ville = models.CharField(max_length=20, default=None, blank=True)
    telephone = models.CharField(max_length=10, default=None, blank=True)


    @staticmethod
    def get_url(img=None, default=None):
        if img:
            return reverse_lazy('url_public', args=(img.name[2:]
                                                    if img.name.startswith('./')
                                                    else img.name,))
        if default:
            return static(default)
        return static('img/no-image-yet.jpg')

    def __str__(self):
        return "{}".format(self.user)
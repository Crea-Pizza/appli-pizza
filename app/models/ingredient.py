from django.db import models


class Ingredient(models.Model):
    label = models.CharField(max_length=200,
                             null=True,
                             blank=True,
                             default=None)

    def __str__(self):
        return "{}".format(self.label)

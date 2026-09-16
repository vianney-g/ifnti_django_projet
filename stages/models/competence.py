from django.db import models


class Competence(models.Model):
    libelle = models.CharField("libellé", max_length=80, unique=True)

    class Meta:
        ordering = ["libelle"]
        verbose_name = "compétence"

    def __str__(self):
        return self.libelle

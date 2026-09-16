from django.db import models


class Personne(models.Model):
    """Ce qu'ont en commun toutes les personnes du domaine. Aucune table ne lui correspond."""

    class Sexe(models.TextChoices):
        FEMININ = "F", "Féminin"
        MASCULIN = "M", "Masculin"

    nom = models.CharField(max_length=80)
    prenom = models.CharField("prénom", max_length=80)
    sexe = models.CharField(max_length=1, choices=Sexe)
    date_naissance = models.DateField("date de naissance")
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True
        ordering = ["nom", "prenom"]

    def __str__(self):
        return f"{self.prenom} {self.nom}"

from django.db import models

from .competence import Competence
from .entreprise import Entreprise


class Offre(models.Model):
    entreprise = models.ForeignKey(
        Entreprise, on_delete=models.PROTECT, related_name="offres"
    )
    titre = models.CharField(max_length=150)
    description = models.TextField()
    date_debut = models.DateField("début du stage")
    date_fin = models.DateField("fin du stage")
    nb_places = models.PositiveSmallIntegerField("nombre de places", default=1)
    competences = models.ManyToManyField(
        Competence,
        related_name="offres",
        blank=True,
        verbose_name="compétences demandées",
    )

    class Meta:
        ordering = ["-date_debut", "titre"]

    def __str__(self):
        return f"{self.titre} — {self.entreprise.nom}"

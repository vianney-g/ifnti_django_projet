from django.db import models

from .etudiant import Etudiant
from .offre import Offre


class Candidature(models.Model):
    class Statut(models.TextChoices):
        DEPOSEE = "deposee", "Déposée"
        RETENUE = "retenue", "Retenue"
        REFUSEE = "refusee", "Refusée"

    etudiant = models.ForeignKey(
        Etudiant, on_delete=models.CASCADE, related_name="candidatures"
    )
    offre = models.ForeignKey(
        Offre, on_delete=models.CASCADE, related_name="candidatures"
    )
    date_depot = models.DateField("date de dépôt", auto_now_add=True)
    statut = models.CharField(max_length=10, choices=Statut, default=Statut.DEPOSEE)

    class Meta:
        ordering = ["-date_depot"]
        constraints = [
            models.UniqueConstraint(
                fields=["etudiant", "offre"], name="une_candidature_par_offre"
            ),
        ]

    def __str__(self):
        return f"{self.etudiant} → {self.offre.titre}"

from django.db import models

from .entreprise import Entreprise
from .personne import Personne


class TuteurEntreprise(Personne):
    """La personne qui encadre le stagiaire dans l'entreprise."""

    entreprise = models.ForeignKey(
        Entreprise, on_delete=models.PROTECT, related_name="tuteurs"
    )

    class Meta(Personne.Meta):
        verbose_name = "tuteur en entreprise"
        verbose_name_plural = "tuteurs en entreprise"

from django.db import models

from .candidature import Candidature
from .enseignant_referent import EnseignantReferent
from .tuteur_entreprise import TuteurEntreprise


class Stage(models.Model):
    """Un stage naît d'une candidature retenue, et d'une seule."""

    candidature = models.OneToOneField(
        Candidature, on_delete=models.PROTECT, related_name="stage"
    )
    tuteur_entreprise = models.ForeignKey(
        TuteurEntreprise, on_delete=models.PROTECT, related_name="stages"
    )
    enseignant_referent = models.ForeignKey(
        EnseignantReferent, on_delete=models.PROTECT, related_name="stages"
    )
    sujet = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.sujet} ({self.candidature.etudiant})"

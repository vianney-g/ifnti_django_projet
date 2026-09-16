from django.db import models

from .competence import Competence
from .personne import Personne


class Etudiant(Personne):
    matricule = models.CharField(max_length=20, unique=True)
    promotion = models.PositiveSmallIntegerField(
        help_text="Année de sortie, par exemple 2027."
    )
    competences = models.ManyToManyField(
        Competence, related_name="etudiants", blank=True, verbose_name="compétences"
    )

    class Meta(Personne.Meta):
        verbose_name = "étudiant"

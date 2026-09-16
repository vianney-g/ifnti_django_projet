from .personne import Personne


class EnseignantReferent(Personne):
    """L'enseignant de l'IFNTI qui suit le stage."""

    class Meta(Personne.Meta):
        verbose_name = "enseignant référent"
        verbose_name_plural = "enseignants référents"

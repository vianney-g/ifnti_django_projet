from django.contrib import admin

from .models import (
    Candidature,
    Competence,
    EnseignantReferent,
    Entreprise,
    Etudiant,
    Offre,
    Stage,
    TuteurEntreprise,
)


@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ["nom", "ville", "secteur"]
    search_fields = ["nom", "ville"]


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    search_fields = ["libelle"]


@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ["nom", "prenom", "matricule", "promotion"]
    list_filter = ["promotion"]
    search_fields = ["nom", "prenom", "matricule"]


@admin.register(TuteurEntreprise)
class TuteurEntrepriseAdmin(admin.ModelAdmin):
    list_display = ["nom", "prenom", "entreprise"]


@admin.register(EnseignantReferent)
class EnseignantReferentAdmin(admin.ModelAdmin):
    list_display = ["nom", "prenom", "email"]


@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ["titre", "entreprise", "date_debut", "date_fin", "nb_places"]
    list_filter = ["entreprise"]


@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ["etudiant", "offre", "date_depot", "statut"]
    list_filter = ["statut"]


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ["sujet", "candidature", "tuteur_entreprise", "enseignant_referent"]

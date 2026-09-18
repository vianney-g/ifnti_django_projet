from django.shortcuts import get_object_or_404, render

from ..models import Entreprise


def liste_entreprises(request):
    return render(
        request,
        "stages/liste_entreprises.html",
        {"entreprises": Entreprise.objects.all()},
    )


def detail_entreprise(request, pk):
    entreprise = get_object_or_404(Entreprise, pk=pk)
    return render(
        request,
        "stages/detail_entreprise.html",
        {
            "entreprise": entreprise,
            # Les offres de l'entreprise, avec leurs compétences : sans le
            # prefetch, le gabarit repartirait chercher les compétences offre
            # par offre.
            "offres": entreprise.offres.prefetch_related("competences"),
        },
    )

import datetime

import pytest

from stages.models import Competence, Entreprise, Offre


@pytest.fixture
def offre(db):
    entreprise = Entreprise.objects.create(
        nom="Sokodé Numérique",
        ville="Sokodé",
        secteur="Services informatiques",
        contact="contact@sokode-numerique.example",
    )
    offre = Offre.objects.create(
        entreprise=entreprise,
        titre="Développeur Django junior",
        description="Stage de fin d'études.",
        date_debut=datetime.date(2027, 4, 5),
        date_fin=datetime.date(2027, 6, 25),
        nb_places=2,
    )
    offre.competences.add(Competence.objects.create(libelle="Django"))
    return offre


def test_la_liste_des_offres_montre_l_entreprise(client, offre):
    contenu = client.get("/").content.decode()

    assert offre.titre in contenu
    assert offre.entreprise.nom in contenu


def test_le_detail_d_une_offre_montre_ses_competences(client, offre):
    contenu = client.get(f"/offres/{offre.pk}/").content.decode()

    assert "Django" in contenu


def test_une_offre_inexistante_repond_404(client, db):
    assert client.get("/offres/9999/").status_code == 404


def test_le_detail_d_une_entreprise_liste_ses_offres(client, offre):
    contenu = client.get(f"/entreprises/{offre.entreprise.pk}/").content.decode()

    assert offre.titre in contenu
    assert "Django" in contenu

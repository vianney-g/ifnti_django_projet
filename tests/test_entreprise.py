import pytest

from stages.models import Entreprise


@pytest.fixture
def entreprise(db):
    return Entreprise.objects.create(
        nom="Cabinet Zongo",
        ville="Sokodé",
        secteur="Comptabilité",
        contact="contact@zongo.tg",
    )


def test_str_affiche_le_nom_et_la_ville(entreprise):
    assert str(entreprise) == "Cabinet Zongo (Sokodé)"


def test_la_liste_affiche_les_entreprises(client, entreprise):
    reponse = client.get("/entreprises/")

    assert reponse.status_code == 200
    assert "Cabinet Zongo" in reponse.content.decode()

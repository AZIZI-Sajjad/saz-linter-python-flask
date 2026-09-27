import pytest
from app import app

@pytest.fixture
def client_app():
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_helth(client_app):
    res = client_app.get("/health")
    assert res.status_code == 200

def test_hello(client_app):
    res = client_app.get("/hello")
    assert res.status_code == 200

# Les tests /health et /hello vérifient juste que Flask répond :
# ils passent toujours.
# Le test /dbtest vérifie la connexion à la BDD : c'est un test d'intégration.
# Il ne passe que si tout le docker compose tourne, sinon il fait échouer
# toute la suite.
# L'idée : marquer ce test avec un flag (@pytest.mark.integration)
# pour lancer les deux types séparément.
@pytest.mark.integration
def test_dbtest(client_app):
    res = client_app.get("/dbtest")
    assert res.status_code == 200
    json_data = res.get_json()
    assert json_data.get("db_connection") == "successful"

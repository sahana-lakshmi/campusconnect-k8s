
from app import app


def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.json["application"] == "CampusConnect"


def test_events():
    response = app.test_client().get("/events")
    assert response.status_code == 200
    assert len(response.json) == 3


def test_successful_registration():
    response = app.test_client().post(
        "/register",
        json={"name": "Student", "event_id": 1}
    )
    assert response.status_code == 201
    assert response.json["message"] == "Registration successful"


def test_missing_registration_details():
    response = app.test_client().post("/register", json={})
    assert response.status_code == 400


def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

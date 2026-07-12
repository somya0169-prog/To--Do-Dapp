import pytest

from app import app, tasks


@pytest.fixture(autouse=True)
def clear_tasks():
    tasks.clear()
    yield
    tasks.clear()


def test_index_displays_empty_state():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert "No tasks yet" in html


def test_add_and_delete_tasks():
    client = app.test_client()

    add_response = client.post("/add", data={"task": "Buy milk"}, follow_redirects=True)
    assert add_response.status_code == 200
    html = add_response.get_data(as_text=True)
    assert "Buy milk" in html

    delete_response = client.get("/delete/0", follow_redirects=True)
    assert delete_response.status_code == 200
    html = delete_response.get_data(as_text=True)
    assert "No tasks yet" in html

import pytest

@pytest.fixture
def client_app():
    from farmapp import app
    app.app.config['TESTING'] = True
    yield app.app.test_client()
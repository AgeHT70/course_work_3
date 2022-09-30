import pytest
import run


# создаем фикстуру для тестирования всех вьюшек
@pytest.fixture()
def test_client():
    app = run.app
    app.config['JSON_AS_ASCII'] = False
    return app.test_client()

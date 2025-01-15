import pytest
from driver import iniciar_driver

@pytest.fixture
def driver():
    driver = iniciar_driver()
    yield driver
    driver.quit()

def test_abrir_homepage(driver):
    driver.get("https://www.mercadolivre.com.br")
    assert "Mercado Livre" in driver.title

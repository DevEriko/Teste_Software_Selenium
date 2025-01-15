import time

def test_tempo_carregamento_homepage(driver):
    start_time = time.time()
    driver.get("https://www.mercadolivre.com.br")
    end_time = time.time()
    tempo_carregamento = end_time - start_time
    assert tempo_carregamento < 3  # A página deve carregar em menos de 3 segundos

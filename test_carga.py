import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def iniciar_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def teste_carga(driver):
    driver.get("https://www.mercadolivre.com.br")
    assert "Mercado Livre" in driver.title
    driver.quit()  # Fecha o driver após o teste

def testar_carga():
    threads = []
    for i in range(5):  # Simula 5 usuários simultâneos
        driver = iniciar_driver()  # Inicia um novo driver para cada thread
        thread = threading.Thread(target=teste_carga, args=(driver,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Aguarda todas as threads terminarem

if __name__ == "__main__":
    testar_carga()


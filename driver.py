from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def iniciar_driver():
    # Usa o WebDriver Manager para garantir que a versão correta do ChromeDriver seja usada
    service = Service(executable_path="C:\\Users\\Andressa\\Desktop\\Teste Selenium\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

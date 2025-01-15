def test_pesquisa_funcionando(driver):
    driver.get("https://www.mercadolivre.com.br")
    barra_de_pesquisa = driver.find_element("name", "as_word")
    barra_de_pesquisa.send_keys("notebook")
    barra_de_pesquisa.submit()
    assert "notebook" in driver.page_source

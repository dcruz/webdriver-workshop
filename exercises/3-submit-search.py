#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
=====================
3. Submit search
=====================
Submissão de uma pesquisa
Validação de que a pesquisa retorna resultados
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Import para inserção de teclas especiais

# Escolha do conector de Webdriver
driver = webdriver.Firefox()
#driver = webdriver.Chrome('./lib/chromedriver')

# Pesquisa a submeter
query = 'adfasfasfasfasfsfdsfar5435234534545afgasfadasf'

# Abrir a homepage do SAPO
driver.get('http://www.sapo.pt/');

# Localizar o campo de pesquisa
elem = driver.find_element_by_name("q")

# Escrever o termo de pesquisa no campo
elem.send_keys(query)

# Submeter o formulário de pesquisa simulando a tecla ENTER
elem.send_keys(Keys.ENTER)

# Validar que a expressão "Sem resultados" não aparece na página
# 'page_source' corresponde ao código da página enviado pelo servidor
assert "Sem resultados" not in driver.page_source

# Fecha a conexão com o browser
driver.close()

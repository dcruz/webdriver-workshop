#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
=====================
2. Click link
=====================
Submissão de uma pesquisa
Validação de que a pesquisa retorna resultados
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Import para inserção de teclas especiais

# Escolha do conector de Webdriver
driver = webdriver.Firefox()
#driver = webdriver.Chrome('./lib/chromedriver')

# Abrir a homepage do SAPO
driver.get('http://www.sapo.pt/');

# Localizar o campo de pesquisa
elem = driver.find_element_by_css_selector("#categoria-tecnologia")

# Confirmar que se navegou para a página de notícias de tecnologia
active_tab = driver.find_element_by_css_selector('.active')

print active_tab.text
assert "Tecnologia" == active_tab.text

# Fecha a conexão com o browser
driver.close()

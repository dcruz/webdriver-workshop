#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
=====================
2. Click link
=====================
Clique no separador de Tecnologia
Certificar-se que se está na página de Tecnologia
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Import para inserção de teclas especiais
import time

# Escolha do conector de Webdriver
driver = webdriver.Firefox()
#driver = webdriver.Chrome('./lib/chromedriver')

# Abrir a homepage do SAPO
driver.get('http://www.sapo.pt/');

# Localizar o campo de pesquisa
elem = driver.find_element_by_css_selector("#categoria-tecnologia")
# -> o que falta?

# Confirmar que se navegou para a página de notícias de tecnologia
active_tab = driver.find_element_by_css_selector('.active')

print active_tab.text
assert "Tecnologia" == active_tab.text

# Fecha a conexão com o browser
driver.close()

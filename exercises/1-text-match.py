#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
=====================
1. Text match
=====================
Verifica se o texto do título(<h1>) é o esperado
"""

from selenium import webdriver

# Título esperado
expected_title = 'SAPO'

# Escolha do conector de Webdriver
driver = webdriver.Firefox()
#driver = webdriver.Chrome('./lib/chromedriver')

# Abrir a homepage do SAPO
driver.get('http://www.sapo.pt/');

# Localizar o campo de pesquisa
elem = driver.find_element_by_id("logo")

# Título é igual ao esperado?
assert elem.text == expected_title

# Fecha a conexão com o browser
driver.close()

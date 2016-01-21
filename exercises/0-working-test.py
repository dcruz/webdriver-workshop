#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
=====================
0. Working test
=====================
Caso básico de teste de Selenium/Webdriver
Deverá abrir o browser e passar com sucesso
"""

from selenium import webdriver

# Escolha do conector de Webdriver
driver = webdriver.Firefox()
#driver = webdriver.Chrome('./lib/chromedriver')

# Opening a page
driver.get('http://www.sapo.pt/');

# Testar se o título é "SAPO"
# Lança um erro se não fôr
assert "SAPO" == driver.title

# Fecha a conexão com o browser
driver.close()

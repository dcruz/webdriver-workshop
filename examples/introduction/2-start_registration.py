#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
=====================
1. Go to registration page
=====================
Abre o widget de email e clica para criar registo
Certifica-se que está na página de registo
"""

from selenium import webdriver

# Escolha do conector de Webdriver
driver = webdriver.Firefox()
#driver = webdriver.Chrome('./lib/chromedriver')

# Opening a page
driver.get('http://www.sapo.pt/');

# Testar se o título é "SAPO"
assert "SAPO" == driver.title

# Certificar-se que o widget de email está fechado
mail_widget = driver.find_element_by_css_selector('#mail')
assert not mail_widget.is_displayed()

# Abrir o widget de email
mail_btn = driver.find_element_by_css_selector('#widgets .mail')
mail_btn.click()

# Certificar-se que o widget de email está visível
assert mail_widget.is_displayed()

# Localizar o link de registo dentro do widget
# E clicar nele
register_link = mail_widget.find_element_by_css_selector('.section-footer a')
register_link.click()

# Certificar-se que se está na página de registo
assert u"Criação" in driver.title

# Fecha a conexão com o browser
driver.close()

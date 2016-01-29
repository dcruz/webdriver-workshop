#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
=====================
1. Open email widget
=====================
Selecciona o widget e clica nele.
Verifica que o widget de email abriu.
"""

from selenium import webdriver
import time

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

time.sleep(5)

# Certificar-se que o widget de email está visível
assert mail_widget.is_displayed()

# Fecha a conexão com o browser
driver.close()

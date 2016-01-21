#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
=====================
4. Multiple locators
=====================
Uso de múltiplos selectores com estratégias de pesquisa diferentes (CSS e XPath)
E possível usar uma pesquisa por elmento para resintringir o espectro de pesquisa a uma sub-árvore do página.
Desta forma é possível adequar-se a precisão e abstracção da estratégia de localização.
"""

from selenium import webdriver
import time

# Escolha do conector de Webdriver
driver = webdriver.Firefox()
#driver = webdriver.Chrome('./lib/chromedriver')

# Abrir a página
driver.get('http://aiaiai.dk/')

# Localizar a sidebar usando um selector de CSS
sidebar = driver.find_element_by_css_selector('.sidebar')

# Localizar o link 'About e clicar nele
# Usa-se um selector XPath que só procura dentro da sub-árvore '.sidebar'
elem = sidebar.find_element_by_xpath('//ul/li[5]')

elem.click() # clicar no link 'About'

time.sleep(3)

# Validar que se cliou no link 'About'
assert elem.text == 'About'

# Fecha a conexão com o browser
driver.close()

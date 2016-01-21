#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
=====================
AVANÇADO: Subscrição newsletter lifestyle
=====================
Este exercícios avançado é para proceder ao preenchimento
da modal de subscrição do SAPO Lifestyle
"""

from selenium import webdriver
import time


# Escolha do conector de Webdriver
driver = webdriver.Firefox()
#driver = webdriver.Chrome('./lib/chromedriver')

"""
Não alterar
<start> Injecção do cookie para abrir a modal
"""
driver.get('http://lifestyle.sapo.pt/404');

new_cookie = {'name' : '_ckiemsg', 'value' : '1', 'path' : '/'}
driver.add_cookie(new_cookie)

for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])

driver.get('http://lifestyle.sapo.pt/')

"""
<end>
"""


# 1.Esperar que a modal de newsletter apareça
#   sem usar usar coisas como 'time.sleep()'

# 2.Preencher o email

# 3.Escolher o género (interagir com o objecto "Select")

# 4.Preencher a data de nascimento

# 5.Não autorizar a partilha de dados

# 6.Submeter

#
# Extra pontos: preencher a data
# interagindo com o 'datepicker'
#

time.sleep(2)

# Fecha a conexão com o browser
driver.close()

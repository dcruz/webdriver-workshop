#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
=====================
5. Selectors mayhem
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
driver.get('http://mag.sapo.pt/')

#
# 1
#
# TODO: abrir a página de nomeados aos Óscares
# interagindo com o menu

#
# 2
#
# TODO: Código com erro. Corrigir
melhor_filme = driver.find_element_by_css_selector('.nominees h4')
print melhor_filme.text
assert 'MELHOR FILME' == melhor_filme.text

primeiro_nomeado = driver.find_element_by_css_selector('.nominees .details li:nth-of-type(0)')
print primeiro_nomeado.text
assert 'A Ponte' in primeiro_nomeado.text

#
# 3
#
# - Abrir a lista de filmes
# - Navegar para a letra "Q"
# - Garantir que o filme "Quarto" é o único filme

#
# 4
#
# - Abrir a página de detalhe do filme "Quarto"
# - Pôr o vídeo a reproduzir

# Fecha a conexão com o browser
driver.close()

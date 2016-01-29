#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
=====================
4. Wait for email validation
=====================
No caso anterior, era provável que a validação de email não tivesse concluído.
Esperamos explicitamente pela validação durante 10s e preenchemos com outros dados
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Escolha do conector de Webdriver
driver = webdriver.Firefox()
#driver = webdriver.Chrome('./lib/chromedriver')
wait = WebDriverWait(driver, 10)

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
assert "email SAPO" in driver.title

# Preenche o campo de nome
name_field = driver.find_element_by_name('name')
name_field.send_keys(u'João Silva')

# Preenche email
email_field = driver.find_element_by_name('email')
email_field.send_keys('joaosilva')

# Verifica que o email não está disponível
#email_error = driver.find_element_by_css_selector('#registo .control-group:nth-of-type(2) .setMsg.error')
email_error = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#registo .control-group:nth-of-type(2) .setMsg.error')
        ))
assert email_error.is_displayed()

time.sleep(5)

# Preenche um email válido
email_field.clear()
email_field.send_keys('chefe-joao-silva')
assert not email_error.is_displayed()

time.sleep(5)

# Fecha a conexão com o browser
driver.close()

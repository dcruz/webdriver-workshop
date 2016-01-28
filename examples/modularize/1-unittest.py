#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
=====================
6. Modularizar com unittest
=====================
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select # Adicionar para lidar com selects
import time

class TestRegistration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome('./lib/chromedriver')
        #wait = WebDriverWait(driver, 10)

    def setUp(self):
        self.driver.get('http://www.sapo.pt/');

    def test_widget_opens(self):
        # Certificar-se que o widget de email está fechado
        mail_widget = self.driver.find_element_by_css_selector('#mail')
        self.assertFalse(mail_widget.is_displayed(), 'Mail widget is opened')

        # Abrir o widget de email
        mail_btn = self.driver.find_element_by_css_selector('#widgets .mail')
        mail_btn.click()

        # Certificar-se que o widget de email está visível
        self.assertTrue(mail_widget.is_displayed())

    def test_open_registration_page(self):
        # Certificar-se que o widget de email está fechado
        mail_widget = self.driver.find_element_by_css_selector('#mail')
        self.assertFalse(mail_widget.is_displayed())

        # Abrir o widget de email
        mail_btn = self.driver.find_element_by_css_selector('#widgets .mail')
        mail_btn.click()

        # Localizar o link de registo dentro do widget
        # E clicar nele
        register_link = mail_widget.find_element_by_css_selector('.section-footer a')
        register_link.click()

        # Certificar-se que se está na página de registo
        self.assertIn("email SAPO", self.driver.title)

    def test_fill_birthdate(self):
        self.driver.get('https://mail.sapo.pt/registo/')

        # Preencher a data de aniversário
        birthdate_day = Select(self.driver.find_element_by_name('day'))
        birthdate_month = Select(self.driver.find_element_by_name('month'))
        birthdate_year = Select(self.driver.find_element_by_name('year'))

        birthdate_day.select_by_index(7)
        birthdate_month.select_by_visible_text('Jun')
        birthdate_year.select_by_value('1984')

        time.sleep(5)

    def tearDown(self):
        # Não estamos a usar
        # Mantemos o browser aberto para os testes seguintes
        pass

    @classmethod
    def tearDownClass(cls):
        # Fecha a conexão com o browser
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

from behave import *
import time

@given('I open SAPO homepage')
def step_impl(context):
    context.browser.get("http://sapo.pt/")

@when('I search for "{query}"')
def step_impl(context, query):
    context.query = query
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('q').send_keys(query)
    form.submit()

@when('I load text into search box')
def step_impl(context):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('q').send_keys(context.text)
    form.submit()

@then('Title is SAPO')
def step_impl(context):
    time.sleep(1)
    assert context.browser.title == "SAPO"

@then('SERP "{result_query}" is the same')
def step_impl(context, result_query):
    form = context.browser.find_element_by_name('q')
    assert form.get_attribute('value') == result_query
    
@then('SERP query is the same')
def step_impl(context):
    form = context.browser.find_element_by_name('q')
    assert form.get_attribute('value') == context.query


@then('search box is the same')
def step_impl(context):
    form = context.browser.find_element_by_name('q')
    repr(context.text)
    assert form.get_attribute('value') == context.text

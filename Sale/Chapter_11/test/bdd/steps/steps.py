from lettuce import *
from webtest import TestApp
from nose.tools import assert_equal, assert_in
from bank.bank_app import app, BANK
from bank.account import Account
import requests

@step(u'I create account "([^"]*)" with balance of "([^"]*)"')
def i_create_account_with_balance_of_group1(step, account_number, balance):
    a = Account(account_number, balance)
    BANK.add_account(a)

@step(u'I create the following account:')
def i_create_the_following_account(step):
    for row in step.hashes:
        a = Account(row['account_number'], row['balance'])
        BANK.add_account(a)

@step(u'I visit the homepage')
def i_visit_the_homepage(step):
    world.browser = TestApp(app)
    world.response = world.browser.get('http://localhost:5000/')
    assert_equal(world.response.status_code, 200)

@step(u'I enter the account number "([^"]*)"')
def i_enter_the_account_number_group1(step, account_number):
    form = world.response.forms['account-form']
    form['account_number'] = account_number
    world.form_response = form.submit()
    assert_equal(world.form_response.status_code, 200)

@step(u'And enter username "([^"]*)"')
def and_enter_username_group1(step, username):
    form = world.response.forms['account-form']
    form['username'] = username

@step(u'And enter password "([^"]*)"')
def and_enter_password_group1(step, password):
    form = world.response.forms['account-form']
    form['password'] = password

@step(u'I click login')
def and_i_click_login(step):
    world.response.click()

@step(u'I see a balance of "([^"]*)"')
def i_see_a_balance_of_group1(step, expected_balance):
    assert_in("Balance: {}".format(expected_balance), world.form_response.text)

@step(u'I ping "([^"]*)"')
def given_i_ping_http_frontend_com(step, url):
    world.response = requests.get(url)
    print world.response

@step(u'I receive a successful response')
def then_i_receive_a_successful_response(step):
    assert_equal(world.response.status_code, 200)
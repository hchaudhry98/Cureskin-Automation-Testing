from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@given("Open cart page")
def open_cart_page(context):
    context.app.cart_page.open_cart()


@when("Click to Continue Shopping")
def click_continue_shopping_btn(context):
    context.app.cart_page.click_continue_shopping()


@when("Click on login link")
def click_login_btn(context):
    context.app.cart_page.click_login_btn()


@then("Verify User is taken to all products")
def verify_page_all_products(context):
    context.app.cart_page.verify_url_contains_query("/collections/all")


@then("Verify user is taken to login")
def verify_page_login(context):
    context.app.cart_page.verify_url_contains_query("/account/login")

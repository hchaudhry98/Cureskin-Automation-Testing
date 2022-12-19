from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@when("Click to Shop All")
def click_shop_all_btn(context):
    context.app.main_page.click_shop_all()


@when("Click to Page 2")
def click_page_2(context):
    context.app.shop_page.click_page_2()


@then("Verify that there are no test products")
def verify_test_products(context):
    context.app.shop_page.get_all_products()
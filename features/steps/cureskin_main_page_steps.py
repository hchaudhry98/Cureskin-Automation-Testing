from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@given("Open main page")
def open_main_page(context):
    context.app.main_page.open_main()


@then("Verify contact number is correct")
def verify_contact_number(context):
    context.app.main_page.verify_contact_text("Call us at (080) 4680 9361(Mon-Sat, 10AM – 7PM)Email: hello@cureskin.com")


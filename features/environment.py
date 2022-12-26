from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from features.app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    # below code is for headless mode
    # opt = Options()
    # opt.add_argument("--window-size=1920,1080")
    # opt.add_argument("--start-maximized")
    # opt.add_argument("--headless")

    # context.driver = webdriver.Chrome(chrome_options=opt)
    # context.browser = webdriver.Safari()

    # for BrowserStack
    desired_cap = {
        'bstack:options': {
            "osVersion": "16",
            "deviceName": "iPhone 14",
            "local": "false",
        },
    }
    bs_user = 'hammadchaudhry_oAslhI'
    bs_key = 'GCqY6d8c2eYHzRqkWpNA'
    url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

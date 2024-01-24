from datetime import datetime
from myConfig import SCREENSHOT_PATH
import decorator
import os


# collection area
CANDY_JAR_IMG = '//img[@alt="Candy Jar"]'
COLLECT_BTN = "//button[@data-target='points.button']"
CLOCK_IMG = "//i[@class='far fa-clock']"
COLLECTION_TEXT = "//div[@class='mb-2 font-weight-bold']"
POINTS_BALANCE = "//div[@data-target='points.balance']"
# main page
HIGHLIGHTS = '//span[contains(text(),"Highlights")]'
CHAINS = '//span[contains(text(),"Chains")]'
LOGIN_BTN = '//button[@data-action="click->auth#openSignInModal"]'
CTN_GMAIL = "//div[@id='sign-in']//a[1]//button[1]"
EMAIL_GM = "//input[@id='identifierId']"
EMAIL_NEXT_BTN = "//div[@id='identifierNext']"
PASS_GM = "//input[@type='password']"
PASS_NEXT_BTN = "//*[@id='passwordNext']/div/button/span"
# logout area
USER_BTN = "//i[@class='fa-user fa-fw far']"
SIGN_OUT = "//span[@data-url='/account/sign_out?locale=en']"
SIGN_OUT_SUCCESS_TEXT = "//div[contains(text(),'Signed out successfully')]"
REQUEST_REJECTED_TEXT = "//h1"


def get_screenshot(driver, path):
    screenshot_file = os.path.join(
        path, f"failed_test_{(datetime.now()).strftime('%Y-%m-%d %H:%M:%S')}.png"
    )
    driver.save_screenshot(screenshot_file)
    print(f"Screenshot captured: {screenshot_file}")



def decorator_screenshot(func):
    def wrapper(func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            get_screenshot(args[0], SCREENSHOT_PATH)
            raise

    return decorator.decorator(wrapper, func)

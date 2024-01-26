import logging
import random
import time
import pytest
from signin import Sign_in
from collect_candy import Candy
from signout import Signout
from utils import decorator_screenshot
from myConfig import user_credential

logger = logging.getLogger(__name__)
# Provde your coingecko email and password
# You can provide more than one coingecko account in the user_credentiial
# Always make sure the email and the paswword exist
user_credentials = [(email, password) for email, password in user_credential.items()]
secs = random.randint(1, 12)


@decorator_screenshot
@pytest.mark.parametrize("email, password", user_credentials, ids=["user1", "user2"])
def test_gecko_bot(driver, email, password):
    time.sleep(secs)
    # signing in with password and email
    signin = Sign_in()
    signin.login(email, password, driver)

    # #clickimg the candy to collect the candy
    collect_candy = Candy()
    collect_candy.candy_click(driver)

    # #sigining ou the user
    logger.info("Signing out")
    signout_func = Signout()
    signout_func.logout(email, driver)

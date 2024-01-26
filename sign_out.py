import utils
from sign_in import By, time, logging

class Signout: #signing out user 
   
    def logout(self, email, driver):
        logger = logging.getLogger(__name__)
        try:
            self.email = email
            #locating the dropdown for signing out
            self.profile=driver.find_element(By.XPATH, utils.USER_BTN)
            self.profile.click()
            self.out=driver.find_element(By.XPATH, utils.SIGN_OUT)
            self.out.click()
            time.sleep(3)
            self.sign_out=driver.find_element(By.XPATH, utils.SIGN_OUT_SUCCESS_TEXT)
            logger.info(f'{self.email} coingecko account successfully signed out')
            time.sleep(3)
            driver.close()
        except:
            self.wrong_way=driver.find_element(By.XPATH, utils.REQUEST_REJECTED_TEXT)
            wrong_logout=self.wrong_way.text
            logger.warning(f"Wrong logout: {wrong_logout}")
            driver.close()
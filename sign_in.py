from selenium.webdriver.common.by import By
import utils
import time
import logging


class Sign_in:
    
    def login(self, email, password, driver):
        logger = logging.getLogger(__name__)
        self.email = email
        self.password = password

            
        try:
            #login section on coin
            logger.info(f'Starting of login process')
            time.sleep(8)
            self.user=driver.find_element(By.XPATH, utils.LOGIN_BTN)
            self.user.click()
            #gmail section
            time.sleep(3)
            self.user=driver.find_element(By.XPATH, utils.CTN_GMAIL)
            self.user.click()
            time.sleep(3)
            self.user=driver.find_element(By.XPATH, utils.EMAIL_GM)
            self.user.clear()
            self.user.send_keys(self.email)
            time.sleep(3)
            self.next_p=driver.find_element(By.XPATH, utils.EMAIL_NEXT_BTN)
            self.next_p.click()
            time.sleep(3)
            self.google_pass=driver.find_element(By.XPATH, utils.PASS_GM)
            self.google_pass.clear()
            self.google_pass.send_keys(self.password)
            time.sleep(4)
            self.next_bt=driver.find_element(By.XPATH, utils.PASS_NEXT_BTN)
            self.next_bt.click()
            time.sleep(3)
            logger.info(f'{self.email} coingecko acount is logged in.')
        except:
            logger.error("Login attempt failed")
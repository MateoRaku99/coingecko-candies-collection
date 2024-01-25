import re
from signin import By, time
import utils
import logging


class Candy:
    logger = logging.getLogger(__name__)
#locating and clicking the candy 

    
    def candy_click(self, driver):
        
        self.candy_notify=driver.find_element(By.XPATH, utils.CANDY_JAR_IMG)
        self.candy_notify.click()
        time.sleep(4)

        try:
            #clicking on candy button
            self.candy_collect=driver.find_element(By.XPATH, utils.COLLECT_BTN)
            candies_no=self.candy_collect.text
            candies_collection=self.extract_number_of_candies(candies_no)
            time.sleep(4)
            self.candy_collect.click()
            self.logger.info(f'Today you received {candies_collection}')
            time.sleep(3)
            self.get_points_balance(driver)
        except:
            self.logger.info(f"Candies already collected.")
            self.candy_collected=driver.find_element(By.XPATH, utils.CLOCK_IMG)
            self.candies_count=driver.find_element(By.XPATH, utils.COLLECTION_TEXT)
            candies_no = self.candies_count.text
            collected_candies = self.extract_number_of_candies(candies_no)
            self.logger.info(f"Today you collected: {collected_candies}")
            self.get_points_balance(driver)
    
    
    def extract_number_of_candies(self, text_element):       
        pattern = re.compile(r'\b\d+\b')
        # Use the regex pattern to find the match
        match = pattern.findall(text_element)
        if match:
            extracted_part = match[0]
            return extracted_part
        else:
            self.logger.info("Not able to extract text :(")
            
    def get_points_balance(self, driver):
        self.candies_balance=driver.find_element(By.XPATH, utils.POINTS_BALANCE)
        points_bln=self.candies_balance.text
        self.logger.info(f'Your current balance is: {points_bln}')
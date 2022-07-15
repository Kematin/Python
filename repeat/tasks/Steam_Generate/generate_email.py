# Selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Other modules
from time import sleep
import datetime
from generate_data import GenerateData as GDa

class GenerateEmail:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def __press_element(self, xpath: str):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.find_element(by=By.XPATH, value=xpath).click()
        sleep(2)

    def __send_keys(self, key: str, xpath: str):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.find_element(by=By.XPATH, value=xpath).send_keys(key)
        sleep(2)

    def __get_data(self) -> list[str | str | str]: # email, password, secret word
        g_password = GDa()
        email = g_password.generate_email()
        password = g_password.generate_password(20)
        secret = g_password.generate_secret_word()
        return [email, password, secret]

    def main(self):
        url = 'https://mail.rambler.ru/?utm_source=head&utm_campaign=self_promo&utm_medium=header&utm_content=mail'
        self.driver.get(url)

        frame = '//div[@id="root"]//iframe'
        value = '//a[@class="styles_link___lR7s styles_link__lCdad"]'
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, frame)))
        self.__press_element(value)

        # values
        email, password, secret = self.__get_data()
        frame = '//div[@role="application"]//iframe'
        login = '//input[@id="login"]'
        new_password = '//input[@id="newPassword"]'
        confirm_password = '//input[@id="confirmPassword"]'
        secret_word = '//input[@id="answer"]'

        # send keyses
        self.__send_keys(email, login) # email
        self.__send_keys(password, new_password) # password
        self.__send_keys(password, confirm_password) # password
        self.__send_keys(secret, secret_word) # secret word

        answer = '//input[@class="rui-Input-input rui-Select-field rui-Select-darkPlaceholder"]'


    def write_file(self, values: list[str | str | str]):
        pass


def test():
    pass

def start():
    s = Service(executable_path='driver/geckodriver.exe')
    driver = webdriver.Firefox(service=s)
    try:
        g_email = GenerateEmail(driver)
        g_email.main()
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()



if __name__ == '__main__':
    start()

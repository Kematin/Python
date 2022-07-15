# Selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Other modules
from time import sleep
import datetime
from datetime import time
from datetime import datetime
from generate_data import GenerateData as GDa

class GenerateEmail:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def __press_element(self, xpath: str):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.find_element(by=By.XPATH, value=xpath).click()
        sleep(3)

    def __send_keys(self, key: str, xpath: str):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.find_element(by=By.XPATH, value=xpath).send_keys(key)
        sleep(3)

    def __get_data(self) -> list[str | str | str]: # email, password, secret word
        g_password = GDa()
        email = g_password.generate_email()
        password = g_password.generate_password(20)
        secret = g_password.generate_secret_word()
        return [email, password, secret]

    def check_captcha(self, xpath):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        captcha = self.driver.find_element(by=By.XPATH, value=xpath)
        aria = captcha.get_attribute('aria-checked')
        if aria == 'false': return False 
        else: return True

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

        # manual captcha solution
        frame = '//div[@class="styles_container__fjEe2"]//iframe'
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, frame)))

        captcha = '//div[@id="checkbox"]'
        result = self.check_captcha(captcha)
        while not result:
            sleep(4)
            result = self.check_captcha(captcha)
            print('Captcha not was solution')
        print('Captcha was solution')

        # change value answer
        # frame = '//div[@role="application"]//iframe'
        # self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, frame)))
        # answer = '//input[@class="rui-Input-input rui-Select-field rui-Select-darkPlaceholder"]'
        # answer = self.driver.find_element(by=By.XPATH, value=answer)
        # self.driver.execute_script("arguments[0].value = 'Любимое блюдо';", answer)

        # Press continue
        frame = '//div[@role="application"]//iframe'
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, frame)))
        print('Find frame')

        button = '//button[@class="rui-Button-button rui-Button-type-primary rui-Button-size-medium rui-Button-iconPosition-left rui-Button-block"]'
        self.__press_element(button)
        print('Email was registration')

        # Write file
        self.write_file(email, password, secret)


    def write_file(self, email: str, password: str, secret_word: str):
        time_now = datetime.now().strftime('%H:%M:%S')
        day, month = datetime.now().day, datetime.now().month
        data = f'{time_now}---{day}---{month}'
        with open('Data/email.txt', 'a', encoding='utf-8') as file_:
            text = f'''
{data}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
email: {email}
password: {password}
secret word: {secret_word}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            '''
            file_.write(text)


def test_write_file():
    s = Service(executable_path='driver/geckodriver.exe')
    driver = webdriver.Firefox(service=s)
    try:
        g_email = GenerateEmail(driver)
        g_email.write_file('Email', 'Password', 'Secret word')
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()

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
    # test_write_file()
    start()

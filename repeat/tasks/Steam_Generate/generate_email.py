# Selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Other modules
from time import sleep
from generate_password import GeneratePassword as GPa

class GenerateEmail:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def __press_element(self, frame, xpath):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, frame)))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.find_element(by=By.XPATH, value=xpath).click()
        sleep(5)

    def __send_keys(self, key, frame, value):
        pass

    def __get_data(self) -> list[str | str | str]:
        pass

    def main(self):
        url = 'https://mail.rambler.ru/?utm_source=head&utm_campaign=self_promo&utm_medium=header&utm_content=mail'
        self.driver.get(url)
        frame = '//div[@id="root"]//iframe'
        value = '//a[@class="styles_link___lR7s styles_link__lCdad"]'
        self.__press_element(frame, value)

    def write_file(self):
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

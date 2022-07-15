# Selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Generate
from generate_email import GenerateEmail as GEm
from generate_data import GenerateData as GDa
from generate_phone import GeneratePhone as GPh
from generate_steam import GenerateSteam as GSt

# Other modules
import datetime
from time import sleep


class Generate:
    def __init__(self, driver):
        self.driver = driver

    def main(self):
        g_email = GEm(self.driver)
        g_email.main()

    def write_csv(self):
        pass


def test():
    pass


def start():
    s = Service(executable_path='driver/geckodriver.exe')
    driver = webdriver.Firefox(service=s)
    try:
        gen = Generate(driver)
        gen.main()
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    start()

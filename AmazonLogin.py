from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class Drivers:
    ser_obj = Service('C:\Program Files\Drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=ser_obj)
    driver.get('https://www.amazon.in/')
    driver.maximize_window()


class Amazon(Drivers):

    def amazon_login(self):
        self.driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()
        self.driver.find_element(By.NAME, 'email').send_keys('9182046293')
        self.driver.find_element(By.ID, 'continue').click()
        self.driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('seshu@0235')
        self.driver.find_element(By.ID, 'signInSubmit').click()
        print("Login Successfully")

    def amazon_logout(self):
        self.driver.find_element(By.XPATH, '//*[@id="nav-logo-sprites"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="nav-main"]/div[1]').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign').click()
        print("Logout Successfully !")

    def search(self, kk):
        self.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(kk)
        self.driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()
        print("searched successfully")

    def sort_by(self):
        self.driver.find_element(By.ID, 'a-autoid-0-announce').click()
        self.driver.find_element(By.ID, 's-result-sort-select_2').click()
        time.sleep(3)
        self.amazon_logout()


A = Amazon()
A.amazon_login()
A.search("mobiles")
A.sort_by()

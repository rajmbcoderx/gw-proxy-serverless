import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Note: TO be changed as per environment
# CHROME_DRIVER_LOCATION = "D:\chromedriver_win32\chromedriver.exe"
CHROME_DRIVER_LOCATION = "/usr/local/bin/chromedriver"


class SolutionLinkVerificationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_LOCATION)
        cls.driver.maximize_window()

    def setUp(self):

        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(30)


    def test_SolutionFileTrustEmailPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        # wait for element to appear, then hover it
        wait = WebDriverWait(self.driver, 30)
        solutions_tab = wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/header/div/div/div[2]/nav/div[1]/ul/li[2]/a')))
        ActionChains(self.driver).move_to_element(solutions_tab).perform()

        # wait for file_trust_link menu item to appear, then click it
        file_trust_link = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, '//*[@id="menu-item-558"]/a')))
        file_trust_link.click()
        file_trust_link_page_label = self.driver.find_element_by_xpath("//*[@id='main']/div/div[1]/div/div[1]/section/div/div/div[1]/h2")
        print(file_trust_link_page_label.text)
        self.assertEqual(file_trust_link_page_label.text, "FileTrust for Email", "FileTrust page has wrong label")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/filetrust-for-email/", "FileTrust for Email Page not Opened")

    def test_SolutionFileTrustSDKPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        # wait for element to appear, then hover it
        wait = WebDriverWait(self.driver, 30)
        solutions_tab = wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/header/div/div/div[2]/nav/div[1]/ul/li[2]/a')))
        ActionChains(self.driver).move_to_element(solutions_tab).perform()

        # wait for file_trust_link menu item to appear, then click it
        file_trust_sdk_link = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, '//*[@id="menu-item-557"]/a')))
        file_trust_sdk_link.click()
        file_trust_sdk_link_page_label = self.driver.find_element_by_xpath("//*[@id='main']/div/div[1]/div/div[1]/section/div/div/div[1]/h2")
        print(file_trust_sdk_link_page_label.text)
        self.assertEqual(file_trust_sdk_link_page_label.text, "FileTrust SDK", "FileTrust SDK page has wrong label")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/filetrust-sdk/", "FileTrust SDK for Email Page not Opened")

    def test_SolutionFileTrustCrossDomainPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        # wait for element to appear, then hover it
        wait = WebDriverWait(self.driver, 30)
        solutions_tab = wait.until(
            ec.visibility_of_element_located((By.XPATH, '/html/body/header/div/div/div[2]/nav/div[1]/ul/li[2]/a')))
        ActionChains(self.driver).move_to_element(solutions_tab).perform()

        # wait for file_trust_link menu item to appear, then click it
        cross_domain_link = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, '//*[@id="menu-item-1203"]/a')))
        cross_domain_link.click()
        cross_domain_link_page_label = self.driver.find_element_by_xpath(
            "//*[@id='main']/div/div[1]/div/div[1]/section/div/div/div[1]/h2")
        print(cross_domain_link_page_label.text)
        self.assertEqual(cross_domain_link_page_label.text, "Cross Domain Solutions", "Cross Domain page has wrong label")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/cross-domain-solutions/",
            "Cross Domain Page not Opened")


    #def tearDown(self):
    #    self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

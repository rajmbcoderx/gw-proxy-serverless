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



class ResourcesLinkVerificationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_LOCATION)
        cls.driver.maximize_window()

    def setUp(self):

        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(30)


    def test_CEOBlogPostPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        # wait for element to appear, then hover it
        wait = WebDriverWait(self.driver, 20)
        resources_tab = wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/header/div/div/div[2]/nav/div[1]/ul/li[3]/a')))
        ActionChains(self.driver).move_to_element(resources_tab).perform()

        # wait for file_trust_link menu item to appear, then click it
        ceo_blog_link = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, '//*[@id="menu-item-1226"]/a')))
        ceo_blog_link.click()
        ceo_blog_link_page_label = self.driver.find_element_by_xpath("//*[@id='main']/div/div/section/div/div/div/h2")
        print(ceo_blog_link_page_label.text)
        self.assertEqual(ceo_blog_link_page_label.text, "CEO Blog", "FileTrust page has wrong label")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/ceo-blog/", "CEO Blog Post Page not Opened")

    def test_CustomerSuccessStoriesPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        # wait for element to appear, then hover it
        wait = WebDriverWait(self.driver, 20)
        resources_tab = wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/header/div/div/div[2]/nav/div[1]/ul/li[3]/a')))
        ActionChains(self.driver).move_to_element(resources_tab).perform()

        # wait for ceo_blog_link menu item to appear, then click it
        customer_success_stories_link = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, '//*[@id="menu-item-1227"]/a')))
        customer_success_stories_link.click()
        customer_success_stories_link_page_label = self.driver.find_element_by_xpath("//*[@id='main']/div/div/section/div/div/div/h2")
        print(customer_success_stories_link_page_label.text)
        self.assertEqual(customer_success_stories_link_page_label.text, "Success Stories", "Success Stories page has wrong label")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/customer-success-stories/", "Customer Success Stories for Email Page not Opened")

    def test_ThreatIntelligencePage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        # wait for element to appear, then hover it
        wait = WebDriverWait(self.driver, 20)
        resources_tab = wait.until(
            ec.visibility_of_element_located((By.XPATH, '/html/body/header/div/div/div[2]/nav/div[1]/ul/li[3]/a')))
        ActionChains(self.driver).move_to_element(resources_tab).perform()

        # wait for ceo_blog_link menu item to appear, then click it
        threat_intelligence_link = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, '//*[@id="menu-item-1228"]/a')))
        threat_intelligence_link.click()
        threat_intelligence_link_page_label = self.driver.find_element_by_xpath(
            "//*[@id='main']/div/div/section/div/div/div/h2")
        print(threat_intelligence_link_page_label.text)
        self.assertEqual(threat_intelligence_link_page_label.text, "Threat Intelligence", "Threat Intelligence page has wrong label")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/threat-intelligence/",
            "Threat Intelligence Page not Opened")


    def test_TechBlogPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        # wait for element to appear, then hover it
        wait = WebDriverWait(self.driver, 20)
        resources_tab = wait.until(
            ec.visibility_of_element_located((By.XPATH, '/html/body/header/div/div/div[2]/nav/div[1]/ul/li[3]/a')))
        ActionChains(self.driver).move_to_element(resources_tab).perform()

        # # wait for ceo_blog_link menu item to appear, then click it
        # tech_blog_link = WebDriverWait(self.driver, 20).until(
        #     ec.visibility_of_element_located((By.XPATH, '//*[@id="menu-item-1229"]/a')))
        # tech_blog_link.click()
        # tech_blog_link_page_label = self.driver.find_element_by_xpath(
        #     "//*[@id='_obv.shell._surface_1584889829954']/div/div[3]/div[1]/div[1]/header/div/div/div[2]/a/h1")
        # print(tech_blog_link_page_label.text)
        # self.assertEqual(tech_blog_link_page_label.text, "Glasswall Engineering", "tech Blog page has wrong label")
        # self.assertEqual(self.driver.current_url, "https://medium.com/glasswall-engineering",
        #     "Tech Blog Page not Opened")

    def test_GlassWallFileDropPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        # wait for element to appear, then hover it
        wait = WebDriverWait(self.driver, 20)
        resources_tab = wait.until(
            ec.visibility_of_element_located((By.XPATH, '/html/body/header/div/div/div[2]/nav/div[1]/ul/li[3]/a')))
        ActionChains(self.driver).move_to_element(resources_tab).perform()

        # wait for ceo_blog_link menu item to appear, then click it
        glasswall_file_drop_link = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, '//*[@id="menu-item-2125"]/a')))
        glasswall_file_drop_link.click()
        glasswall_file_drop_link_page_label = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div[2]/h1")
        print(glasswall_file_drop_link_page_label.text)
        self.assertEqual(glasswall_file_drop_link_page_label.text, "Drag and drop a file to have it processed by the Glasswall d-FIRST™ Engine", "Glasswall File Drop page has wrong label")
        self.assertEqual(self.driver.current_url, "https://glasswall-file-drop.azurewebsites.net/",
            "Glasswall Engineering Page not Opened")

    #def tearDown(self):
    #    self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
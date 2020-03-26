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


class FooterLinkVerificationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_LOCATION)
        cls.driver.maximize_window()

    def setUp(self):

        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)

    def test_TechnologyFirstLink_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//*[@id='menu-item-345']/a").click()
        technologyPageLabel = self.driver.find_element_by_xpath("//*[@id='main']/div/div[1]/section/div/div/div[1]/h2")
        print(technologyPageLabel.text)
        self.assertEqual(technologyPageLabel.text, "Introducing d-FIRST™", "Technology Page not Opened")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/technology/",
                         "Technology Page not Opened")

    def test_SolutionFileTrustEmailPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//*[@id='menu-item-1222']/a").click()
        file_trust_link_page_label = self.driver.find_element_by_xpath("//*[@id='main']/div/div[1]/div/div[1]/section/div/div/div[1]/h2")
        print(file_trust_link_page_label.text)
        self.assertEqual(file_trust_link_page_label.text, "FileTrust for Email", "FileTrust page has wrong label")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/filetrust-for-email/", "FileTrust for Email Page not Opened")

    def test_SolutionFileTrustSDKPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//*[@id='menu-item-1223']/a").click()
        file_trust_sdk_link_page_label = self.driver.find_element_by_xpath("//*[@id='main']/div/div[1]/div/div[1]/section/div/div/div[1]/h2")
        print(file_trust_sdk_link_page_label.text)
        self.assertEqual(file_trust_sdk_link_page_label.text, "FileTrust SDK", "FileTrust SDK page has wrong label")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/filetrust-sdk/", "FileTrust SDK for Email Page not Opened")

    def test_SolutionFileTrustCrossDomainPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//*[@id='menu-item-1221']/a").click()
        cross_domain_link_page_label = self.driver.find_element_by_xpath(
            "//*[@id='main']/div/div[1]/div/div[1]/section/div/div/div[1]/h2")
        print(cross_domain_link_page_label.text)
        self.assertEqual(cross_domain_link_page_label.text, "Cross Domain Solutions", "Cross Domain page has wrong label")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/cross-domain-solutions/",
            "Cross Domain Page not Opened")


    def test_CEOBlogPostPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//*[@id='menu-item-563']/a").click()
        ceo_blog_link_page_label = self.driver.find_element_by_xpath("//*[@id='main']/div/div/section/div/div/div/h2")
        print(ceo_blog_link_page_label.text)
        self.assertEqual(ceo_blog_link_page_label.text, "CEO Blog", "FileTrust page has wrong label")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/ceo-blog/", "CEO Blog Post Page not Opened")

    def test_CustomerSuccessStoriesPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//*[@id='menu-item-561']/a").click()
        customer_success_stories_link_page_label = self.driver.find_element_by_xpath("//*[@id='main']/div/div/section/div/div/div/h2")
        print(customer_success_stories_link_page_label.text)
        self.assertEqual(customer_success_stories_link_page_label.text, "Success Stories", "Success Stories page has wrong label")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/customer-success-stories/", "Customer Success Stories for Email Page not Opened")

    def test_ThreatIntelligencePage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//*[@id='menu-item-564']/a").click()
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
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//*[@id='menu-item-1224']/a").click()
        tech_blog_link_page_label = self.driver.find_element_by_xpath(
            "//div[starts-with(@id,'_obv.shell._surface_')]/div/div[3]/div[1]/div[1]/header/div/div/div[2]/a/h1")
        print(tech_blog_link_page_label.text)
        self.assertEqual(tech_blog_link_page_label.text, "Glasswall Engineering", "tech Blog page has wrong label")
        self.assertEqual(self.driver.current_url, "https://medium.com/glasswall-engineering",
            "Tech Blog Page not Opened")

    def test_CompanyPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//*[@id='menu-item-347']/a").click()
        companyPageLabel = self.driver.find_element_by_xpath("//*[@id='main']/div/div/div/section/div/div/div/h2")
        print(companyPageLabel.text)
        self.assertEqual(companyPageLabel.text, "Who We Are", "Company Page not Opened")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/company/", "Company Page not Opened")


    def test_PartnersPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//*[@id='menu-item-346']/a").click()
        partnersPageLabel = self.driver.find_element_by_xpath("//*[@id='main']/div/div/section/div/div/div/h2")
        print(partnersPageLabel.text)
        self.assertEqual(partnersPageLabel.text, "Partners", "Partners Page not Opened")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/partners/", "Partners Page not Opened")


    def test_ContactPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//*[@id='menu-item-676']/a").click()
        contactPageLabel = self.driver.find_element_by_xpath("//*[@id='main']/div/section/div/div/div[1]/h1")
        print(contactPageLabel.text)
        self.assertEqual(contactPageLabel.text, "Contact Glasswall", "Contact Page not Opened")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/contact/", "Contact Page not Opened")

    #def tearDown(self):
    #    self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
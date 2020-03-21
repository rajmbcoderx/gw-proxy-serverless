import unittest
from selenium import webdriver


# Note: TO be changed as per environment
# CHROME_DRIVER_LOCATION = "D:\chromedriver_win32\chromedriver.exe"
CHROME_DRIVER_LOCATION = "/usr/local/bin/chromedriver"


class LinkVerifictionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_LOCATION)
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(30)

    def test_TechnologyPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.find_element_by_xpath("/html/body/header/div/div/div[2]/nav/div[1]/ul/li[1]/a").click()
        technologyPageLabel = self.driver.find_element_by_xpath("//*[@id='main']/div/div[1]/section/div/div/div[1]/h2")
        print(technologyPageLabel.text)
        self.assertEqual(technologyPageLabel.text, "Introducing d-FIRST™", "Technology Page not Opened")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/technology/",
                         "Technology Page not Opened")

    def test_SolutionsPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.find_element_by_xpath("/html/body/header/div/div/div[2]/nav/div[1]/ul/li[2]/a").click()
        solutionPageLabel = self.driver.find_element_by_xpath("//*[@id='main']/div/div[1]/section/div/div/div[1]/h2")
        print(solutionPageLabel.text)
        self.assertEqual(solutionPageLabel.text, "Solutions", "Solutions Page not Opened")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/solutions/",
                         "Solutions Page not Opened")

    def test_ResourcesPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.find_element_by_xpath("/html/body/header/div/div/div[2]/nav/div[1]/ul/li[3]/a").click()
        resourcesPageLabel = self.driver.find_element_by_xpath("//*[@id='main']/div/section/div/div/div[1]/h2")
        print(resourcesPageLabel.text)
        self.assertEqual(resourcesPageLabel.text, "CEO BLOG", "Resources Page not Opened")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/resources/",
                         "Resources Page not Opened")

    def test_PartnersPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.find_element_by_xpath("/html/body/header/div/div/div[2]/nav/div[1]/ul/li[4]/a").click()
        partnersPageLabel = self.driver.find_element_by_xpath("//*[@id='main']/div/div/section/div/div/div/h2")
        print(partnersPageLabel.text)
        self.assertEqual(partnersPageLabel.text, "Partners", "Partners Page not Opened")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/partners/",
                         "Partners Page not Opened")

    def test_CompanyPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.find_element_by_xpath("/html/body/header/div/div/div[2]/nav/div[1]/ul/li[5]/a").click()
        companyPageLabel = self.driver.find_element_by_xpath("//*[@id='main']/div/div/div/section/div/div/div/h2")
        print(companyPageLabel.text)
        self.assertEqual(companyPageLabel.text, "Who We Are", "Company Page not Opened")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/company/", "Company Page not Opened")

    def test_ContactPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.find_element_by_xpath("/html/body/header/div/div/div[2]/nav/div[2]/ul/li[3]/a").click()
        contactPageLabel = self.driver.find_element_by_xpath("//*[@id='main']/div/section/div/div/div[1]/h1")
        print(contactPageLabel.text)
        self.assertEqual(contactPageLabel.text, "Contact Glasswall", "Contact Page not Opened")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/contact/", "Contact Page not Opened")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

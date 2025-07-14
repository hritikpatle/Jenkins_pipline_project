from selenium import webdriver
import unittest

class DemoPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_title(self):
        self.driver.get("file://" + "index.html")
        self.assertIn("Demo", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

import unittest
import theCrag_to_UKC_crag_converter as converter
import time
from selenium.webdriver.common.by import By

test_url = "https://www.thecrag.com/en/climbing/australia/hornsby-and-the-north/area/1375085595"

class TestRoutesCSV(unittest.TestCase):

    def test_get_fa(self):
        routes = get_test_routes()
        fa_info = converter.get_fa(routes[3])
        
        self.assertEqual(fa_info.what, "FA")
        self.assertEqual(fa_info.who, "Jack Schyvens & Daniel Butler")
        self.assertEqual(fa_info.when, "22 Jul 2017")

if __name__ == "__main__":
    unittest.main()

def get_test_routes():
    driver = converter.set_up_scrape()
    driver.get(test_url)
    time.sleep(5)  # Wait for the page to load completely
    routes = driver.find_elements(By.CLASS_NAME, "route")
    return routes

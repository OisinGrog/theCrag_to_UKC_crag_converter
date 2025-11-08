import unittest
import theCrag_to_UKC_crag_converter as converter
import time
from selenium.webdriver.common.by import By

local_site = "file:///C:/Users/oisin/Coding%20Projects/theCrag_to_UKC_crag_converter/tests/test_site.html"

class TestRoutesCSV(unittest.TestCase):

    def test_scrape_route(self):
        routes = converter.scrape_route(local_site)
        test_route = routes[0]

        self.assertEqual(test_route.name, "Hidey-Hole")
        self.assertEqual(test_route.climb_type, "Boulder")
        self.assertEqual(test_route.grade, "V0")
        self.assertEqual(test_route.stars, 1)
        self.assertEqual(test_route.height, "6m")
        self.assertEqual(test_route.description, "Starting from the left hand side, climb almost diagonal towards the hole near the top. (Where a nice no hands rest is available). From here its just a matter of standing up to reach a jug and then over the top.")
        self.assertIsNone(test_route.bolts)
        self.assertIsNotNone(test_route.fa)
        self.assertIsNone(test_route.pitches)

    def test_get_fa(self):
        routes = converter.scrape_route(local_site)
        test_route = routes[0]
        
        self.assertEqual(test_route.fa.what, "FA:")
        self.assertEqual(test_route.fa.who, "Jack Schyvens & Daniel Butler")
        self.assertEqual(test_route.fa.when, "22 Jul 2017")
    
if __name__ == "__main__":
    unittest.main()

def get_local_test_routes():
    driver = converter.set_up_scrape()
    driver.get("file:///C:/Users/oisin/Coding%20Projects/theCrag_to_UKC_crag_converter/tests/test_site.html")
    time.sleep(1)
    routes = driver.find_elements(By.CLASS_NAME, "route")
    return routes   
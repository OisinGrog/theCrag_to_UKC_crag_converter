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
    
    def test_get_ffa(self):
        routes = converter.scrape_route(local_site)
        test_route = routes[1]

        self.assertEqual(test_route.fa.what, "FFA:")
        self.assertEqual(test_route.fa.who, "This guy & That guy")
        self.assertEqual(test_route.fa.when, "22 Jul 2017")

    def test_multi_desc(self):
        routes = converter.scrape_route(local_site)
        test_route = routes[2]

        expected_desc="The aid (originally a few bolts) at the start of the second pitch was freed by Joe Friend. Start 33m right of PV at obvious right trending wide yellow crack/corner system. Marked with J." \
        "30m (18) Stem up featured corner system that funnels into a chimney near the top. Traverse right 4m to semi-hanging belay off rap chains. Lots of long slings useful on this pitch." \
        "60m (22) Burly, slick and spectacular. The right trending wide crack breaching the upper headwall. Climb past optional belay at 30m (dead tree + choss) and trend right across the slab to end at the chains above Blast Off. They are under a little rooflet just beneath the top of the cliff." \
        "Reportedly you can rap from the optional tree belay back to the end of pitch one and then to the ground with a 50m rope, however this tree has died, mostly fallen over, and is no longer suitable to rap off. Instead top out and walk/rap off as per options described above."

        self.assertEqual(test_route.description, expected_desc)

if __name__ == "__main__":
    unittest.main()

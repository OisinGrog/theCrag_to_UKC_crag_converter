import unittest
import theCrag_to_UKC_crag_converter as converter

class TestRoutesCSV(unittest.TestCase):

    def test_get_FA(self):
        description = "A whole lot of random text \n" \
        "FA: John Doe \n" \
        "FFA: Jane Doe \n"

        response = converter.get_FA(description)

        self.assertEqual(response, "John Doe")


if __name__ == "__main__":
    unittest.main()
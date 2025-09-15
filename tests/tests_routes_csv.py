import unittest
import routes_csv, route_info
import os

class TestRoutesCSV(unittest.TestCase):
    
    def setUp(self):
        """Set up a sample route for testing."""
        self.sample_route = route_info.Route(
            name="Test Route",
            climb_type="Sport",
            grade="6a",
            height="20m",
            description="A challenging sport route.",
            bolts=5
        )
    
    def test_write_to_csv(self):
        """Test writing a single route to CSV."""
        routes = [self.sample_route]
        filename = "test_routes.csv"
        
        routes_csv.write_to_csv(routes, filename)
        
        with open(filename, mode='r') as file:
            content = file.readlines()
        
        self.assertEqual(len(content), 2)  # Header + 1 route
        self.assertIn("Test Route", content[1])
        self.assertIn("Sport", content[1])
        self.assertIn("6a", content[1])
        self.assertIn("20m", content[1])
        self.assertIn("A challenging sport route.", content[1])
        self.assertIn("5", content[1])

        os.remove(filename)
        
if __name__ == "__main__":
    unittest.main()
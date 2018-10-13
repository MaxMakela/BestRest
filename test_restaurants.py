from mapsJson import get_best_restaurant
from mapsJson import get_top_best_restaurant
import unittest

class TestRestaurants(unittest.TestCase):

    def test_best_restaurant_1(self):
        restaurants = [
            {"rating": 5.0, "name": "Restr Five"},
            {"rating": 4.4, "name": "Restr Four"},
            {"rating": 3.3, "name": "Restr Three"},
            {"rating": 2.2, "name": "Restr Two"},
            {"rating": 1.0, "name": "Restr One"},
        ]
        r = get_best_restaurant(restaurants)
        self.assertEqual(r["name"], "Restr Five")

    def test_best_restaurant_2(self):
        restaurants = [
            {"rating": 1.0, "name": "Restr One"},
            {"rating": 2.2, "name": "Restr Two"},
            {"rating": 4.4, "name": "Restr Four"},
            {"rating": 3.3, "name": "Restr Three"},
            {"rating": 5.0, "name": "Restr Five"},
        ]
        r = get_best_restaurant(restaurants)
        self.assertEqual(r["name"], "Restr Five")

    def test_best_restaurant_3(self):
        restaurants = [
            {"rating": 1.0, "name": "Restr One"},
            {"rating": 2.2, "name": "Restr Two"},
            {"name": "Restr Four"},
            {"rating": 5.0, "name": "Restr Five"},
            {"rating": 3.3, "name": "Restr Three"},
        ]
        r = get_best_restaurant(restaurants)
        self.assertEqual(r["name"], "Restr Five")

    def test_best_restaurant_4(self):
        restaurants = []
        r = get_best_restaurant(restaurants)
        self.assertEqual(r, None)

    def test_restorans_sorting_1(self):
        restaurants = []
        r = get_top_best_restaurant(restaurants,5)
        self.assertEqual(r, None)

    def test_restorans_sorting_2(self):
        restaurants = [
            {"rating": 1.0, "name": "Restr One"},
            {"rating": 2.2, "name": "Restr Two"},
            {"rating": 4.4, "name": "Restr Four"},
            {"rating": 3.3, "name": "Restr Three"},
            {"rating": 5.0, "name": "Restr Five"},
        ]
        r = get_top_best_restaurant(restaurants, 0)
        self.assertEqual(r[0], {"rating": 5.0, "name": "Restr Five"})

    def test_restorans_sorting_3(self):
        restaurants = [
            {"rating": 1.0, "name": "Restr One"},
            {"rating": 2.2, "name": "Restr Two"},
            {"rating": 4.4, "name": "Restr Four"},
            {"rating": 3.3, "name": "Restr Three"},
            {"rating": 5.0, "name": "Restr Five"},
        ]
        r = get_top_best_restaurant(restaurants, -1)
        self.assertEqual(r[0], {"rating": 5.0, "name": "Restr Five"})

    def test_restorans_sorting_4(self):
        restaurants = [
            {"rating": 1.0, "name": "Restr One"},
            {"rating": 2.2, "name": "Restr Two"},
            {"rating": 4.4, "name": "Restr Four"},
            {"rating": 3.3, "name": "Restr Three"},
            {"rating": 5.0, "name": "Restr Five"},
        ]
        r = get_top_best_restaurant(restaurants, 6)
        self.assertEqual(r, restaurants)

    def test_restorans_sorting_5(self):
        restaurants = [
            {"rating": 1.0, "name": "Restr One"},
            {"rating": 2.2, "name": "Restr Two"},
            {"name": "Restr Four"},
            {"rating": 3.3, "name": "Restr Three"},
            {"rating": 5.0, "name": "Restr Five"},
        ]
        r = get_top_best_restaurant(restaurants, -1)
        self.assertEqual(r[0], {"rating": 5.0, "name": "Restr Five"})

if __name__ == '__main__':
    unittest.main()

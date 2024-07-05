import unittest
from practice15 import Drone


class TestDrone(unittest.TestCase):
    def setUp(self):
        self.drone1 = Drone()

    def test_take_off(self):
        self.drone1.battery_charge = 50
        result = self.drone1.take_off()
        self.assertTrue(self.drone1.is_flying)
        self.assertEqual(result, "Готовность на взлет!")

        self.drone1.battery_charge = 10
        result = self.drone1.take_off()
        self.assertFalse(self.drone1.is_flying)
        self.assertEqual(result, "Заряд батареи слишком низкий для взлета")

    def test_land_not_flying(self):
        self.drone1.is_flying = False
        result = self.drone1.land()
        self.assertFalse(self.drone1.is_flying)
        self.assertEqual(result, "Дрон на земле")

    def test_land_flying(self):
        self.drone1.is_flying = True
        result = self.drone1.land()
        self.assertFalse(self.drone1.is_flying)
        self.assertEqual(result, "Дрон уже приземлился")

if __name__ == "__main__":
    unittest.main()


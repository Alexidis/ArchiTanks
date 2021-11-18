import unittest
from metaObj import MetaTanks, UnBurnFuelObj, DOT
from game import Tank, \
                 Move, Rotate, CheckFuel, BurnFuel, BurnFuelMove, \
                 MovableAdapter, RotatableAdapter, CheckFuelAdapter, BurnFuelAdapter, \
                 CommandException


class TestMotion(unittest.TestCase):
    
    def test_valid_move(self):
        test_t1 = Tank([12, 5])
        test_t1.velocity = [-7, 3]
        Move(MovableAdapter(test_t1)).execute()
        self.assertEqual(test_t1.get_property('position'), [5, 8])

    def test_unreadable_position(self):
        meta_t1 = MetaTanks([12, 5])
        meta_t1.velocity = [-7, 3]
        with self.assertRaises(AttributeError):
            Move(MovableAdapter(meta_t1)).execute()

    def test_unreadable_velocity(self):
        meta_t1 = MetaTanks([12, 5])
        meta_t1.velocity = [-7, 3]
        with self.assertRaises(AttributeError):
            Move(MovableAdapter(meta_t1)).execute()

    def test_unsetable_velocity(self):
        meta_t1 = MetaTanks([12, 5])
        meta_t1.velocity = [-7, 3]
        with self.assertRaises(AttributeError):
            Move(MovableAdapter(meta_t1)).execute()

    def test_valid_rotate(self):
        test_t1 = Tank([12, 5], 110)
        test_t1.angle_velocity = 70
        Rotate(RotatableAdapter(test_t1)).execute()
        self.assertEqual(test_t1.get_property('direction'), 180)

    def test_unreadable_direction(self):
        meta_t1 = MetaTanks([12, 5], 110)
        meta_t1.angle_velocity = 70
        with self.assertRaises(AttributeError):
            Rotate(RotatableAdapter(meta_t1)).execute()

    def test_unreadable_angle_velocity(self):
        meta_t1 = MetaTanks([12, 5], 110)
        meta_t1.angle_velocity = 70
        with self.assertRaises(AttributeError):
            Rotate(RotatableAdapter(meta_t1)).execute()

    def test_unsetable_direction(self):
        meta_t1 = MetaTanks([12, 5], 110)
        meta_t1.angle_velocity = 70
        with self.assertRaises(AttributeError):
            Rotate(RotatableAdapter(meta_t1)).execute()

    def test_unreadable_fuel_on_chk(self):
        meta_obj = DOT([12, 5])
        with self.assertRaises(KeyError):
            CheckFuel(CheckFuelAdapter(meta_obj)).execute()

    def test_fuel_chk(self):
        fuel = 100
        fuel_velocity = 200
        meta_obj = Tank([12, 5], 0, fuel, fuel_velocity)
        with self.assertRaises(CommandException):
            CheckFuel(CheckFuelAdapter(meta_obj)).execute()

    def test_unreadable_fuel_on_burn(self):
        meta_obj = DOT([12, 5])
        with self.assertRaises(KeyError):
            BurnFuel(BurnFuelAdapter(meta_obj)).execute()

    def test_setable_fuel(self):
        meta_obj = UnBurnFuelObj()
        with self.assertRaises(KeyError):
            BurnFuel(BurnFuelAdapter(meta_obj)).execute()

    def test_fuel_chk_fail(self):
        fuel = 100
        fuel_velocity = 200
        meta_obj = Tank([12, 5], 0, fuel, fuel_velocity)
        cm_l = [CheckFuel(CheckFuelAdapter(meta_obj)), Move(MovableAdapter(meta_obj)), BurnFuel(BurnFuelAdapter(meta_obj))]
        with self.assertRaises(CommandException):
            BurnFuelMove(cm_l).execute()


if __name__ == '__main__':
    unittest.main()

import unittest
from game import Tank, Move, Rotate, MovableAdapter, RotatableAdapter


class MetaTanks:
    def __init__(self, position=None, direction=0):
        self.position = position or [0, 0]
        self.velocity = [0, 0]
        self.direction = direction
        self.angle_velocity = 0


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


if __name__ == '__main__':
    unittest.main()

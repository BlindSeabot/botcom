from main import *

import unittest

class Test(unittest.TestCase):
    def testControlDataConstruction(self):
        actual = control(1, 2, 3, 0, 7, 0, 7, 1, 0, 0)
        self.assertEqual(
            actual, b"\xFF\xFE\xFF\xFE\x01\x02\x03\x00\x07\x00\x07\x01\x00\x04\x0f"
        )

    def testStateInfoInit(self):
        raw_data = b"\xff\xfe\xff\xfe\x01\x00\x00\x00\x02\x32\x03\x72\x00\x00\x01\x00\x00\x08\xff\xff\xff\xfc\x00\x01\x1e\x00\x08\xc4"
        state = StateData(StateData.parse_raw_bytes(raw_data))
        self.assertEqual(state.left_motor_speed, 0x100)


unittest.main()


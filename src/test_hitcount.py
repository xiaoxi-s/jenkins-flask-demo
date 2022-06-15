import unittest
from unittest.mock import patch

import mockredis
import hitcount

class HitCountTest(unittest.TestCase):
    @patch('hitcount.r', mockredis.mock_strict_redis_client(host='0.0.0.0', port=6379, db=0))
    def testOneHit(self):
        hitcount.hit('user1')
        self.assertEqual(b'1', hitcount.get_hit('user1'))

if __name__ == '__main__':
    unittest.main()

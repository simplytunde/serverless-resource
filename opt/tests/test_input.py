import unittest
from unittest.mock import MagicMock

import input
import test_common
from serverless import Serverless


class TestInput(unittest.TestCase):
    def setUp(self):
        Serverless.execute_command = MagicMock(name='execute_command')

    def test_invalid_json(self):
        test_common.put_stdin(
            """
            {
              "source": {
                "apiKey": "apiKey123",
                "secretKey": "secretKey321"
              },
              "params": {
              }
            }
            """)

        self.assertEqual(input.execute('/'), -1)

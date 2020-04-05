import unittest
from parsehub.client import ParseHubClient


class TestClient(unittest.TestCase):
    
    def test_init_client(self):
        client = ParseHubClient('dummy_key')
        self.assertEqual('dummy_key', client.token)

if __name__ == '__main__':
    unittest.main()

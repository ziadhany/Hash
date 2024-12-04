import unittest
from main import hash_generator, action_handler

class TestHashApp(unittest.TestCase):
    def test_hash_generator(self):
        result = hash_generator("MD5", b"hello")
        self.assertEqual(result, "5d41402abc4b2a76b9719d911017c592")

        result = hash_generator("SHA1", b"world")
        self.assertEqual(result, "7c211433f02071597741e6ff5a8ea34789abbf43")

if __name__ == "__main__":
    unittest.main()

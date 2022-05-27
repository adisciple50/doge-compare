from unittest import TestCase
from arbitrage.credentials import AuthManager

class TestAuthManager(TestCase):
    def test_load_credentials(self):
        credentials = AuthManager().load_credentials()
        assert isinstance(credentials,bool) or isinstance(credentials,dict)

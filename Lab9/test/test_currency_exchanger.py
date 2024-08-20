# Panyawut Saengdaeng 653380138-3 Sec.1
# Lab9 - Test double
# Integration testing using Mock - Create Mock object to mimic the behavior of external service

import unittest
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from unittest.mock import patch, Mock
# Import CurrencyExchanger class
from source.currency_exchanger import CurrencyExchanger
from utils import get_mock_currency_api_response

class TestCurrencyExchanger(unittest.TestCase):
    def setUp(self):
        self.exchanger = CurrencyExchanger(base_currency="THB", target_currency="KRW")
        self.mock_api_response = get_mock_currency_api_response()

    # Mock the 'requests' package from source.currency_exchanger
    @patch("source.currency_exchanger.requests")
    def test_currency_exchange(self, mock_request):
        # Assign mock's return value
        mock_request.get.return_value = self.mock_api_response

        # Act - execute class under test
        result = self.exchanger.currency_exchange(100)

        # Check whether the mocked method is called
        mock_request.get.assert_called_once()

        # Check whether the mocked method is called with the right parameter
        mock_request.get.assert_called_with(
            "https://coc-kku-bank.com/foreign-exchange",
            params={'from': 'THB', 'to': 'KRW'}
        )

        # Assert the returned responses
        self.assertIsNotNone(self.exchanger.api_response)
        self.assertEqual(self.exchanger.api_response, self.mock_api_response.json())
        self.assertEqual(result, 100 * 38.69)

    @patch("source.currency_exchanger.requests")
    def test_currency_exchange_with_invalid_amount(self, mock_request):
        # Assign mock's return value
        mock_request.get.return_value = self.mock_api_response

        # Act - execute class under test with invalid amount (0)
        result = self.exchanger.currency_exchange(0)

        # Check whether the mocked method is called
        mock_request.get.assert_called_once()

        # Check whether the mocked method is called with the right parameter
        mock_request.get.assert_called_with(
            "https://coc-kku-bank.com/foreign-exchange",
            params={'from': 'THB', 'to': 'KRW'}
        )

        # Assert the returned response (should be 0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()

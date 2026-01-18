import unittest
from unittest.mock import patch, MagicMock
from crawler.main import crawl_headers, filter_headers, evaluate_security

class TestHeaderCrawler(unittest.TestCase):

    @patch('crawler.main.requests.head')
    def test_crawl_headers_success(self, mock_head):
        mock_response = MagicMock()
        mock_response.headers = {'Content-Type': 'text/html', 'Server': 'nginx'}
        mock_head.return_value = mock_response

        headers = crawl_headers('https://example.com')
        self.assertEqual(headers, {'Content-Type': 'text/html', 'Server': 'nginx'})

    @patch('builtins.print')
    @patch('crawler.main.requests.head')
    def test_crawl_headers_error(self, mock_head, mock_print):
        mock_head.side_effect = Exception("Connection error")
        headers = crawl_headers('https://example.com')
        self.assertEqual(headers, {})

    def test_filter_headers(self):
        headers = {'Content-Type': 'text/html', 'Server': 'nginx', 'X-Frame-Options': 'DENY'}
        keys = ['Server', 'X-Frame-Options']
        filtered = filter_headers(headers, keys)
        self.assertEqual(filtered, {'Server': 'nginx', 'X-Frame-Options': 'DENY'})

    def test_evaluate_security_missing_server_header(self):
        headers = {'Content-Type': 'text/html'}
        result = evaluate_security(headers)
        self.assertEqual(result, "Missing Server header")

    def test_evaluate_security_with_server_header(self):
        headers = {'Server': 'nginx/1.18.0'}
        result = evaluate_security(headers)
        self.assertEqual(result, "Webserver: nginx/1.18.0")

if __name__ == "__main__":
    unittest.main()

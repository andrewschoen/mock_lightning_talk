import unittest

from http_stuff import HttpTester
from mock import patch, MagicMock

HTTP_REQUESTS = 1


class MockResponse(object):
    """Mocks a response object
    """
    def __init__(self, content=None, headers=None, status_code=None):
        self.content = content
        self.headers = headers
        self.status_code = status_code

    def __call__(self, *args, **kwargs):
        return self


class HttpTests(unittest.TestCase):
    challenge = "abcdefg"

    def setUp(self):
        self.http = HttpTester()

    def tearDown(self):
        pass

    @patch('requests.get', new_callable=MockResponse, status_code=200)
    def test_200_status(self, mock):
        for i in range(0, HTTP_REQUESTS):
            r = self.http.send_request('http://httpbin.org/status/200')
            self.assertEqual(r.status_code, 200)

    def test_404_status(self):
        with patch('requests.get', new_callable=MockResponse, status_code=404):
            r = self.http.send_request('http://httpbin.org/status/404')
        self.assertEqual(r.status_code, 404)

    @patch.object(HttpTester, 'get_challenge_string')
    @patch('requests.get', new_callable=MockResponse, status_code=200,
           content=challenge)
    def test_challenge_returned(self, mock, mock_get_challenge_string):
        mock_get_challenge_string.return_value = self.challenge
        r = self.http.send_request_with_challenge('http://httpbin.org/get')
        self.assertEqual(r.status_code, 200)
        self.assertTrue(self.challenge in r.content)

    @patch('requests.get', new_callable=MockResponse, status_code=200,
           content=challenge)
    def test_challenge_returned_magic(self, mock):
        self.http.get_challenge_string = MagicMock(return_value=self.challenge)
        r = self.http.send_request_with_challenge('http://httpbin.org/get')
        self.assertEqual(r.status_code, 200)
        self.assertTrue(self.challenge in r.content)


if __name__ == "__main__":
    unittest.main()

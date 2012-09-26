import unittest

from http_stuff import HttpTester

HTTP_REQUESTS = 1


class HttpTests(unittest.TestCase):

    def setUp(self):
        self.http = HttpTester()

    def tearDown(self):
        pass

    def test_200_status(self):
        for i in range(0, HTTP_REQUESTS):
            r = self.http.send_request('http://httpbin.org/status/200')
            self.assertEqual(r.status_code, 200)

    def test_404_status(self):
        r = self.http.send_request('http://httpbin.org/status/404')
        self.assertEqual(r.status_code, 404)

    def test_403_status(self):
        r = self.http.send_request('http://httpbin.org/status/403')
        self.assertEqual(r.status_code, 403)

    def test_challenge_returned(self):
        r = self.http.send_request_with_challenge('http://httpbin.org/get')
        self.assertEqual(r.status_code, 200)


if __name__ == "__main__":
    unittest.main()

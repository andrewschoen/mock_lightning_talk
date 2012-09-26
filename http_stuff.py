import requests
import random

from string import ascii_letters, digits


class HttpTester(object):
    def send_request(self, url):
        r = requests.get(url)
        return r

    def send_request_with_challenge(self, url):
        """Sends request with a random challenge string.

        If the response includes the same string in the body, return
        the response. Otherwise, return False
        """

        challenge = self.get_challenge_string()
        params = {
            "challenge": challenge
        }
        r = requests.get(url, params=params)
        if challenge in r.content:
            return r
        return False

    def get_challenge_string(self):
        """Generates a random challenge string"""
        choices = ascii_letters + digits
        return ''.join(random.choice(choices) for i in xrange(128))

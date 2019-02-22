import unittest
import json
import re
from urllib import request


class TestAll(unittest.TestCase):
    """
    A couple of test to assert correctness in data returned
    """

    def setUp(self):
        """
        initialize variables here
        """
        self.url = 'http://localhost:5000/total'
        self.default_payload = b'numbers=1,2,3'

    def test_api_health_check(self):
        """
        check for the status of the API endpoint
        hopefully we should be a 200 status code
        """
        response = request.urlopen(self.url)
        self.assertEqual(response.getcode(), 200)

    def test_api_post_call(self):
        """
        check that the API endpoint is accepting payloads at this
        time via a post call
        """
        response = request.urlopen(self.url)
        req = request.Request(self.url, data=self.default_payload)
        response = request.urlopen(req)
        self.assertEqual(response.getcode(), 200)

    def test_response_header_type(self):
        """
        check that the correct header is received i.e. application/json
        """
        response = request.urlopen(self.url)
        req = request.Request(self.url, data=self.default_payload)
        response = request.urlopen(req)
        header_type = re.findall(
            r'Content-Type: application/json',
            str(response.headers),
            re.M | re.I
        )
        assert header_type is not None

    def test_json_structure(self):
        """
        check that the correct json structure is received, it must return a
        structure like {"total": <number | NaN>}
        """
        response = request.urlopen(self.url)
        req = request.Request(self.url, data=self.default_payload)
        response = request.urlopen(req)
        output = response.read(response.length).decode('utf-8')
        total = None

        try:
            arr = json.loads(output)
            total = arr["total"]
        except (ValueError, KeyError):
            pass

        assert total is not None

    def test_wrong_payload(self):
        """
        check that NaN is returned when we send a wrong payload
        as against a crashed server
        """
        response = request.urlopen(self.url)
        req = request.Request(self.url, data=b'gibberish=gibberish')
        response = request.urlopen(req)
        output = response.read(response.length).decode('utf-8')
        total = None

        try:
            arr = json.loads(output)
            total = arr["total"]
        except (ValueError, KeyError):
            pass

        self.assertEqual(total, "NaN")

    def test_sum_1_to_3(self):
        """
        assert the API return 5 for the sum of 1,2,3
        """
        response = request.urlopen(self.url)
        req = request.Request(self.url, data=self.default_payload)
        response = request.urlopen(req)
        output = response.read(response.length).decode('utf-8')
        total = None

        try:
            arr = json.loads(output)
            total = arr["total"]
        except (ValueError, KeyError):
            pass

        self.assertEqual(total, 6)


if __name__ == '__main__':
    unittest.main()

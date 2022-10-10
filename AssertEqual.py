import unittest
from unittest import IsolatedAsyncioTestCase
import requests as req

events = []


async def on_cleanup():
    events.append("cleanup")


class AssertEqual(IsolatedAsyncioTestCase):
    def setUp(self):
        events.append("setUp")

    async def test_response(self):
        events.append("test_response")
        resp = req.get("https://www.udemy.com/")
        self.assertNotEqual(resp.status_code, 300)

    def tearDown(self):
        events.append("tearDown")


if __name__ == "__main__":
    unittest.main()

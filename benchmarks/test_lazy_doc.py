import json
import unittest

import bsonjs
from bson_lazy import LazyDoc


class TestItertools(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with open('canada', 'br') as file:
            cls.bson = file.read()
        cls.doc = LazyDoc(cls.bson)

    def test_json(self):
        for i in range(10):
            self.doc.json()


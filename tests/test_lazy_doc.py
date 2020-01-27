import json
import unittest

import bsonjs
from bson_lazy import LazyDoc


class TestItertools(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.dict = {
            'a': 'sdg',
            'b': .5,
            'aihghfasiuhhsdojkhgfhoijhdgh': 8762135476,
            'f': {'fdghgdfh': 763187225, 'dfsgh': 'fd'},
            'd': [1, 2, 3, 4, 45],
        }
        cls.json = json.dumps(cls.dict)
        cls.doc = LazyDoc(bsonjs.loads(cls.json))

    def test_json(self):
        self.assertEqual(
            self.dict,
            json.loads(self.doc.json()),
        )


from time import sleep

import bsonjs


cdef class LazyDoc:
    cdef bytes data

    def __cinit__(self, bytes data):
        self.data = data

    def json(self):
        data = (self.data)
        return bsonjs.dumps(data)


def load(bytes data):
    return LazyDoc(data)

import unittest
import queue

from src import foxlator_lib as fll


class FileSystemMock(fll.utils.FileSystem):
    def __init__(self):
        self.is_file_queue: queue.SimpleQueue[bool] = queue.SimpleQueue()

    def is_file(self, path: str) -> bool:
        if self.is_file_queue.empty():
            return False  # False by default
        return self.is_file_queue.get()

    def push_is_file_return(self, value: bool):
        self.is_file_queue.put(value)


# any utility functions go here
class TestBase(unittest.TestCase):
    pass

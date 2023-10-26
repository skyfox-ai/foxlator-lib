from utils import base

from src import foxlator_lib as fll


class BasicTests(base.TestBase):
    def test_get_version(self):
        """ Test if version has correct format """
        version = fll.utils.get_version()
        parts = version.split('.')
        self.assertEqual(len(parts), 3)
        self.assertTrue(all(map(lambda p: p.isnumeric(), parts)))

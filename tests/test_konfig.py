import os
import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
from konfig import Konfig
from mock import MagicMock


class TestKonf(unittest.TestCase):
    # can be passed a dict
    def test_takes_dict(self):
        kv = {'Foo': 1,
              'Bar': "Two",
              'konf_test': 'Test'}
        konf = Konfig()
        konf.use_dict(kv)
        self.assertEquals('1', konf.Foo)
        self.assertEquals("Two", konf.Bar)
        self.assertEquals('Test', konf.konf_test)

    # checks for environment variable
    def test_reads_environment_variables(self):
        def return_false(arg):
            return False

        def return_kv(arg):
            kv = {'FOO': '1',
                  'BAR': "Two",
                  'KONF_TEST': 'Test'}
            return kv[arg]

        os.path.isfile = MagicMock(name='os_path_isfile',
                                   side_effect=return_false)

        os.getenv = MagicMock(name='os_getenv', side_effect=return_kv)
        konf = Konfig()
        self.assertEquals('1', konf.Foo)
        self.assertEquals("Two", konf.Bar)
        self.assertEquals('Test', konf.konf_test)

    # cheks for .env file in current directory
    def test_looks_for_dotenv_file(self):
        konf = Konfig()
        self.assertEquals('1', konf.Foo)
        self.assertEquals("Two", konf.Bar)
        self.assertEquals('Test', konf.konf_test)

    def test_handles_blank_lines_in_dorenv_file(self):
        return False

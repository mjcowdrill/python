import unittest

from app.file import File

class FileTest(unittest.TestCase):


    def setUp(self):
        self.m_filepath = r"/tmp/ls.d"
        self.m_mode     = "rw"
        self.m_class    = File(self.m_filepath, self.m_mode)

    def test_read_returns_line1(self):

        buffer = "ABC\n"

        f = open(self.m_filepath, "w")
        f.write(buffer)

        self.m_class=File(self.m_filepath, self.m_mode)

        self.assertEquals(buffer, self.m_class.read())

    def test_self_params(self):
        self.m_class.params(1)

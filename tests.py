from unittest import TestCase

from profiler import install_profiler


def add(x, y):
    return x + y


class ProfilerTestCase(TestCase):
    def test_profiler(self):
        install_profiler()
        z = add(1, 2)
        self.assertEqual(z, 3)

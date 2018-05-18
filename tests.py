# -*- coding: utf-8 -*-
"""Run the tests for CoordPy.

This file is simply a test runner for CoordPy. The tests themselves are
in ``coordpy.tests``. The reason we run it from out here is so that the
relative imports work properly.
"""

import unittest

from coordpy.tests import *

if __name__ == '__main__':
    unittest.main()

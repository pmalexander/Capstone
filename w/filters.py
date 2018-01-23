import os 
import unittest
import datetime
from . import app

if not "CONFIG_PATH" in os.environ:
    os.environ["CONFIG_PATH"] = "w.config.TestingConfig"

import w
from w.filters import *

class FilterTests(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
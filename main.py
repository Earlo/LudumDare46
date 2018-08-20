"""
This the Pygearlo, pygame powered GUI, Asset and Event manager system
"""

import sys
from engine import engine

if sys.version_info < (3, 0):
  sys.stdout.write("This program is intended to be used with Python3\n")
  sys.exit(1)

if __name__ == "__main__":
  engine.start()

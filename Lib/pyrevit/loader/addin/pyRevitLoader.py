import os.path as op
import sys

# add the library location to the search paths
sys.path.append(op.dirname(op.dirname(op.dirname(op.dirname(__file__)))))

from pyrevit.loader.sessionmgr import load_session

load_session()

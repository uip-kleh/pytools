import os
import sys
sys.path.append(os.pardir)
from libs.setconfig import SetConfig

class Tools(SetConfig):
    def __init__(self, fname):
        super().__init__(fname)
    
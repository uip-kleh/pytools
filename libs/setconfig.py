import os
import sys
sys.path.append(os.pardir)
import yaml

class SetConfig:
    def __init__(self, fname):
        with open(fname, "r") as f:
            self.args = yaml.safe_load(f)
            set()
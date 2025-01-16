import os
import sys
sys.path.append(os.pardir)
from libs.setconfig import SetConfig

class TestSetConfig(SetConfig):
    def __init__(self, fname):
        super().__init__(fname)
        self.set()
    
    def set(self):
        self.test = self.args["test"]

if __name__ == "__main__":
    fname = "config.yaml"
    setconfig = TestSetConfig(fname)
    print(setconfig.test)
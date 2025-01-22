import os
import sys
sys.path.append(os.pardir)
import pandas as pd

class HandleData:
    def __init__(self):
        pass

    # has header
    def load_csv(self, fname):
        return pd.read_csv(fname, header=0)
    
    # analyse data
    def has_nan(self, df: pd.DataFrame) -> None:
        print("+++ display has nan ? +++")
        print(df.isnull().any())

    def disp_detail(selfs, df: pd.DataFrame) -> None:
        print("+++ display detail of data +++")
        print(df.describe())

if __name__=='__main__':
    pass
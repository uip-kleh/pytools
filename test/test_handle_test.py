import os
import sys
sys.path.append(os.pardir)
import pandas as pd
from libs.handle_data import HandleData

class TestHandleData(HandleData):
    def __init__(self):
        super().__init__()

if __name__=='__main__':
    test_handle_data = TestHandleData()
    fname = "data/data.csv"

    # test loading csv file
    df = test_handle_data.load_csv(fname)
    print(df)

    # test has nan ?
    test_handle_data.has_nan(df)

    # test display detail
    test_handle_data.disp_detail(df)
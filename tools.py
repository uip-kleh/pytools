import os
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from PIL import Image
import json


class BasicTools:
    def __init__(self) -> None:
        pass

    def clear_figure(self):
        plt.clear()
        plt.cla()
        plt.clf()

class IOTools(BasicTools):
    def __init__(self) -> None:
        pass

    def read_csv(self, fname):
        return pd.read_csv(fname)

    def read_image(self, fname, asnumpy=False):
        img = Image.open(fname)
        if asnumpy: return np.array(img)
        return img

    def save_image(self, fname):
        plt.savefig(fname, transparent=True)
        self.clear_figure()

    def save_object(self, obj, fname):
        with open(fname, "w") as f:
            json.dump(obj, f, indent=2)

class Tools(IOTools):
    def __init__(self) -> None:
        super().__init__()

if __name__ == '__main__':
    tools = Tools()
    img = tools.read_color_image("test.jpg", asnumpy=True)
    print(img.shape)



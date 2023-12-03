import os
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from PIL import Image
import json
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator


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

class MLTools(BasicTools):
    def __init__(self) -> None:
        super().__init__()

    class ImageDataFrameGenerator:
        def __init__(self, image_directory, csv_path) -> None:
            self.image_directory = image_directory
            self.csv_path = csv_path

        def load(self, x_col, y_col, test_size=.2, batch_size=256, target_size=(256, 256)):
            df = pd.read_csv(self.csv_path)
            train_df, test_df = train_test_split(
                df,
                test_size=test_size,
                shuffle=True,
                random_state=1
            )

            image_data_gen = ImageDataGenerator(
                rescale=1/255.
            )

            train_gen = image_data_gen.flow_from_dataframe(
                dataframe=train_df,
                directory=self.image_directory,
                shuffle=True,
                seed=0,
                x_col=x_col,
                y_col=y_col,
                target_size=target_size,
                batch_size=batch_size,
                class_mode="gray_scale",
            )

            test_gen = image_data_gen.flow_from_dataframe(
                dataframe=test_df,
                directory=self.image_directory,
                shuffle=False,
                seed=0,
                x_col=x_col,
                y_col=y_col,
                target_size=target_size,
                batch_size=batch_size,
                class_mode="gray_scale",
            )

            return (train_gen, test_gen)

class Tools(IOTools, MLTools):
    def __init__(self) -> None:
        super().__init__()

if __name__ == '__main__':
    tools = Tools()
    img = tools.read_color_image("test.jpg", asnumpy=True)
    print(img.shape)



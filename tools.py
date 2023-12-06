import os
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from PIL import Image
import json
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import f1_score
from keras.preprocessing.image import ImageDataGenerator
from xgboost import XGBClassifier
import pickle


class BasicTools:
    def __init__(self) -> None:
        pass

    def clear_figure(self):
        plt.cla()
        plt.clf()
        plt.close()

    def save_image(self, fname):
        plt.savefig(fname, transparent=True)
        self.clear_figure()

class IOTools(BasicTools):
    def __init__(self) -> None:
        pass

    def read_csv(self, fname):
        return pd.read_csv(fname)

    def read_image(self, fname, asnumpy=False):
        img = Image.open(fname)
        if asnumpy: return np.array(img)
        return img

    def save_object(self, obj, fname):
        with open(fname, "w") as f:
            json.dump(obj, f, indent=2)

class AnalysisTools(BasicTools):
    def __init__(self) -> None:
        super().__init__()

    def extract_objective(self, df: pd.DataFrame, column):
        objective_df = df[column]
        dropped_df = df.drop(column, axis=1)
        return (objective_df, dropped_df)

    def drop_columns(self, df: pd.DataFrame, columns):
        return df.drop(columns, axis=1)

    def has_nan(self, df: pd.DataFrame):
        print(df.isnull().any())

    def fill_nan_with_mode(self, df: pd.DataFrame):
        return df.fillna(df.mode().iloc[0])

    def label_encode(self, train_df: pd.DataFrame, test_df, columns):
        for column in columns:
            le = LabelEncoder()
            le.fit(train_df[column])
            train_df[column] = le.transform(train_df[column])
            test_df[column] = le.transform(test_df[column])
        return (train_df, test_df)

    def onehot_encode(self, labels):
        ohe = OneHotEncoder()
        encoded_label = ohe.fit_transform(labels.reshape(1, -1))
        return encoded_label

    def split_data(self, data, labels):
        return train_test_split(data, labels, stratify=labels, test_size=.2)

class MLTools(BasicTools):
    def __init__(self) -> None:
        super().__init__()

    def microf1_eval(y_pred, dtrain):
        y_true = dtrain.get_label()
        y_pred = np.argmax(y_pred, axis=1)
        err = 1-f1_score(y_true, np.round(y_pred), average="micro")
        return 'f1_err', err

    def generate_cross_index(self, df, labels):
        index = []
        kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)
        for train_idx, val_idx in kf.split(df, labels):
            index.append((train_idx, val_idx))
        return index

    # tensorflow
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

    # XGBoost
    class UseXGBoost:

        def generate_classifier(self):
            return XGBClassifier(n_estimators=1000, tree_method='gpu_hist')

        def save_model(self, model, fname):
            pickle.dump(model, open(fname, "wb"))

        def load_model(self, fname):
            return pickle.load(open(fname, "rb"))

class Tools(IOTools, AnalysisTools, MLTools):
    def __init__(self) -> None:
        super().__init__()

if __name__ == '__main__':
    tools = Tools()
    img = tools.read_color_image("test.jpg", asnumpy=True)
    print(img.shape)



# Documentation

## Basic Tools
- **clear_figure**
  - Clears the Matplotlib pyplot figure.

- **save_image**
  - **Arguments**
    - `fname`: File name
  - Saves the Matplotlib pyplot figure.

## IOTools
- **read_csv**
  - **Arguments**
    - `fname` *(string)*: File name
  - Reads a CSV file and returns a Pandas DataFrame.

- **read_image**
  - **Arguments**
    - `fname` *(string)*: File name
    - `asnumpy` *(bool)*: Read image as a NumPy array
  - Reads a color image.

- **save_object**
  - **Arguments**
    - `obj` *(list, dict)*: Object to save (list or dictionary)
    - `fname` *(string)*: File name
  - Saves a list or dictionary.

## AnalysisTools
- **extract_objective**
  - **Arguments**
    - `df` *(pd.DataFrame)*: Input DataFrame
    - `column` *(string)*: Column to extract
  - Extracts the specified column from a DataFrame.

- **drop_columns**
  - **Arguments**
    - `df` *(pd.DataFrame)*: Input DataFrame
    - `columns` *(list)*: List of columns to drop
  - Drops specified columns from a DataFrame.

- **has_nan**
  - **Arguments**
    - `df` *(pd.DataFrame)*: Input DataFrame
  - Checks and prints if there are any NaN values in the DataFrame.

- **fill_nan_with_mode**
  - **Arguments**
    - `df` *(pd.DataFrame)*: Input DataFrame
  - Fills NaN values in the DataFrame with the mode.

- **label_encode**
  - **Arguments**
    - `train_df` *(pd.DataFrame)*: Training DataFrame
    - `test_df` *(pd.DataFrame)*: Testing DataFrame
    - `columns` *(list)*: List of columns to label encode
  - Label encodes specified columns in both training and testing DataFrames.

- **onehot_encode**
  - **Arguments**
    - `labels` *(array or pd.DataFrame)*: Labels to one-hot encode
  - One-hot encodes labels.

- **split_data**
  - **Arguments**
    - `data` *(array or pd.DataFrame)*: Data to split
    - `labels` *(array or pd.DataFrame)*: Labels for stratified splitting
  - Splits data into training and testing sets.

## DrawTools
- **draw_confusion_matrix**
  - **Arguments**
    - `cm` *(array)*: Confusion matrix
    - `norm` *(bool)*: Normalize the confusion matrix
    - `fname` *(string)*: File name to save the figure
  - Draws and saves the confusion matrix.

## MLTools
- **microf1_eval**
  - Custom evaluation function for XGBoost.

- **generate_cross_index**
  - **Arguments**
    - `df` *(pd.DataFrame)*: DataFrame for cross-validation
    - `labels` *(array or pd.DataFrame)*: Labels for cross-validation
  - Generates cross-validation indices.

- **ImageDataFrameGenerator**
  - **Arguments**
    - `image_directory` *(string)*: Directory path for images
    - `csv_path` *(string)*: Path to the CSV file
  - **Methods**
    - **load**
      - **Arguments**
        - `x_col` *(string)*: A DataFrame column indicating image names
        - `y_col` *(string)*: A DataFrame column indicating labels
        - `test_size` *(float)*: Size of the test set
        - `batch_size` *(int)*: Batch size
        - `target_size` *(tuple)*: Target size for images
  - Loads images into memory per batch using a DataFrame.

- **UseXGBoost**
  - **Methods**
    - **generate_classifier**
      - Generates an XGBoost classifier with default parameters.
    - **save_model**
      - **Arguments**
        - `model`: XGBoost model
        - `fname` *(string)*: File name to save the model
    - **load_model**
      - **Arguments**
        - `fname` *(string)*: File name to load the model from.

## Tools
- A comprehensive set of tools combining functionalities from BasicTools, IOTools, AnalysisTools, DrawTools, and MLTools.

# Documentation

## Basic Tools
- **clear_figure**
  - Clears the Matplotlib pyplot figure.

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

- **save_image**
  - **Arguments**
    - `fname`: File name
  - Saves the Matplotlib pyplot figure.

- **save_object**
  - **Arguments**
    - `obj` *(list, dict)*: Object to save (list or dictionary)
    - `fname` *(string)*: File name
  - Saves a list or dictionary.

## MLTools
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
        - `target` *(tuple)*: Target size for images
  - Loads images into memory per batch using a DataFrame.

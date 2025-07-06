import os 
import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV or Excel file

    Inputs: 
        - file_path (str): path to the data

    Outputs:
        - pd.DataFrame: loaded data
    """
    #check for FileNotFoundError 
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist!!!")
    #extract the file extension
    extension = os.path.splitext(file_path)[1].lower()

    if extension == '.csv':
        df = pd.read_csv(file_path)
    elif extension in ['.xls','.xlsx']:
        df = pd.read_excel(file_path)
    else:
        raise ValueError('Unsupported file format: use CSV or Excel files.')
    
    return df

        

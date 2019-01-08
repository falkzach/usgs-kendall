import pandas as pd

from kendalWrapper import KendallWrapper

if __name__ == "__main__":
    input_path = './Master-NTN-monthly.csv'
    output_path = './results.txt'

    df = pd.read_csv(input_path)
    print(df)
    

import pandas as pd
import csv

# function to write csv file using data from dataframe
def append_df_to_csv(filename, df):

    df = pd.DataFrame(df)    
    print(filename)

    try:
        with open(filename, 'rb') as file:
            writer = csv.writer(file)
            df.to_csv(filename)
    except FileNotFoundError:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            df.to_csv(filename)
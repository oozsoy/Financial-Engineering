import pandas as pd
from glob import glob
import os

# We saved each stock data to different .csv files using get_data.py. They all have the same columns, open, close, vol etc. 
# To differentiate between different stocks, we should indicate ticker name before combining them into one csv file 

files = glob('data/*.csv')

# Check if any files were found
if not files:
    print("No CSV files found in the 'data' directory.")
    exit()

dfs = []

for file in files:
    
    try:
        # read the csv file into a df 
        df = pd.read_csv(file)
    except Exception as e:
        print(f"Error reading the csv {file}: {e}")
        continue 
    
    # Extract the stock symbol from the file name
    try:
        symbol = os.path.basename(file).split('.')[0]
        df['Name'] = symbol
    except Exception as e:
        print(f"Error processing file name {file}: {e}")
        continue
    
    # Append the DataFrame to the list
    dfs.append(df)
    
# Check if any DataFrames were added to the list
if not dfs:
    print("No data was added to the list. Exiting.")
    exit()
    
# Concatenate all DataFrames in the list
try:
    full_df = pd.concat(dfs, ignore_index=True)
except Exception as e:
    print(f"Error concatenating DataFrames: {e}")
    exit()
        
# Save the concatenated DataFrame to a CSV file
try:
    full_df.to_csv('sp500sub.csv', index=False)
    print("Data successfully saved to sp500sub.csv")
except Exception as e:
    print(f"Error saving to CSV: {e}")


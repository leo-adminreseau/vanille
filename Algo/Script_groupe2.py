import pandas as pd

# Read the CSV file
file_path = 'cardata.csv'
delimiter = ';'
df = pd.read_csv(file_path, delimiter=delimiter)

# Display the first few rows
print(df.head())

import pandas as pd

data_frame = pd.read_csv('pokemon_data.csv')

# print(data_frame)
# print(data_frame.head(3))
# print(data_frame.tail(3))

data_frame.columns
data_frame['Name'[0:5]]
data_frame[['Name', 'HP']]
data_frame.iloc[1:4]  # Integer Location to get ROW
data_frame.iloc[2, 1] # Specific ROW, COLUMN

# for index, row in data_frame.iterrows():
#     print(index, row['Name'])

data_frame.loc[data_frame['Type 1'] == 'Fire']  # Based on textual information

data_frame.describe()  # Sorting and Describing



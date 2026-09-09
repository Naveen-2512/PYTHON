import pandas as pd

# Take CSV file name from the user
file_name = input("Enter CSV file name: ")

# Read the CSV file
df = pd.read_csv(file_name)

# Display the data
print("\nCSV Data:")
print(df)

# Display structural dimensions
print("\nNumber of rows and columns:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())

# Display data types
print("\nData Types:")
print(df.dtypes)


# Select a column for filtering
column = input("\nEnter column name for filtering: ")

# Take condition value
value = input("Enter value to filter: ")

# Try numeric filtering if the column contains numbers
try:
    value = float(value)
    filtered_df = df[df[column] == value]
except ValueError:
    filtered_df = df[df[column].astype(str) == value]

# Display filtered data
print("\nFiltered Data:")
print(filtered_df)

# Export the filtered data
output_file = input("\nEnter output CSV file name: ")
filtered_df.to_csv(output_file, index=False)

print("\nFiltered data saved successfully to", output_file)
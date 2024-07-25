import pandas as pd

def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df

def display_first_rows(df, num_rows=5):
    print(df.head(num_rows))

def display_basic_statistics(df):
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['number'])
    
    print("Mean:\n", numeric_df.mean())
    print("Median:\n", numeric_df.median())
    print("Mode:\n", numeric_df.mode().iloc[0])

def filter_dataframe(df, criteria):
    filtered_df = df.query(criteria)
    print(filtered_df)

# Load the DataFrame from CSV
df = load_csv('kidney_disease.csv')

# Display the first few rows
display_first_rows(df)

# Display basic statistics for numeric columns
display_basic_statistics(df)

# Filter the DataFrame based on criteria
filter_dataframe(df, 'age > 50')


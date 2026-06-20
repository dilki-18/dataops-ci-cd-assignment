import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FILE = os.path.join(BASE_DIR, "data", "customers.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "processed")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "cleaned_customers.csv")


def extract():
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(INPUT_FILE)
    return df

def transform(df):

    cleaned_df = df.dropna()
    return cleaned_df

def load(df):

    # Create the 'data/processed' directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(OUTPUT_FILE, index=False)

def main():
    df = extract()
    cleaned_df = transform(df)
    load(cleaned_df)

    print(f"ETL process completed successfully: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

import pandas as pd


def test_no_null_values():

    df = pd.read_csv("data/processed/cleaned_customers.csv")
    assert df.isnull().sum().sum() == 0

    print("Test passed: No null values in the cleaned dataset.")
import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    """Read raw CSV data."""
    return pd.read_csv(file_path)

# Test
if __name__ == "__main__":
    df = extract_data("../../data/raw_sales.csv")
    print(df.head())
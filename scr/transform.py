import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and enrich data."""
    # Add total sales column
    df["total_sales"] = df["quantity"] * df["price"]
    
    # Standardize country codes
    df["country"] = df["country"].replace({"USA": "US", "UK": "GB"})
    
    # Drop duplicates
    df = df.drop_duplicates(subset="order_id")
    
    return df

# Test
if __name__ == "__main__":
    from extract import extract_data
    raw_df = extract_data("../../data/raw_sales.csv")
    clean_df = transform_data(raw_df)
    print(clean_df.head())
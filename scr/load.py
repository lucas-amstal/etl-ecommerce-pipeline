import pandas as pd
from sqlalchemy import create_engine

def load_to_db(df: pd.DataFrame, table_name: str, db_url: str = "sqlite:///sales.db"):
    """Load data into SQL database."""
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists="replace", index=False)

# Test
if __name__ == "__main__":
    from transform import transform_data
    from extract import extract_data
    
    raw_df = extract_data("../../data/raw_sales.csv")
    clean_df = transform_data(raw_df)
    load_to_db(clean_df, "ecommerce_sales")
    print("Data loaded to database!")
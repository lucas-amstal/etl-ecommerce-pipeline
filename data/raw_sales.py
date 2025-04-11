# generate_data.py
import pandas as pd
import numpy as np

data = {
    "order_id": np.arange(1000, 1010),
    "customer_id": np.random.randint(5000, 6000, 10),
    "product": np.random.choice(["Laptop", "Phone", "Tablet", "Headphones"], 10),
    "quantity": np.random.randint(1, 5, 10),
    "price": np.round(np.random.uniform(100, 2000, 10), 2),
    "order_date": pd.date_range("2024-01-01", periods=10),
    "country": np.random.choice(["USA", "UK", "Germany", "Italy"], 10)
}

pd.DataFrame(data).to_csv("data/raw_sales.csv", index=False)
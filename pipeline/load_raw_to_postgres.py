from pathlib import Path
from datetime import datetime, timezone
import os

import pandas as pd
from sqlalchemy import create_engine, text


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "raw" / "olist"

FILES = {
    "olist_customers_dataset.csv": "customers",
    "olist_orders_dataset.csv": "orders",
    "olist_order_items_dataset.csv": "order_items",
    "olist_order_payments_dataset.csv": "payments",
    "olist_products_dataset.csv": "products",
    "product_category_name_translation.csv": "category_translation",
}

DB_URL = os.getenv(
    "RETAIL_DB_URL",
    "postgresql+psycopg2://retail:retail123@127.0.0.1:5432/retail_analytics",
)

engine = create_engine(DB_URL)


def main() -> None:
    loaded_at = datetime.now(timezone.utc)

    with engine.begin() as conn:
        conn.execute(text("create schema if not exists raw"))

    for filename, table_name in FILES.items():
        file_path = DATA_DIR / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Missing file: {file_path}")

        df = pd.read_csv(file_path)
        df["_loaded_at"] = loaded_at

        df.to_sql(
            name=table_name,
            con=engine,
            schema="raw",
            if_exists="replace",
            index=False,
            chunksize=1000,
            method="multi",
        )

        print(f"Loaded {filename} -> raw.{table_name} ({len(df)} rows)")

    print("Raw load complete.")


if __name__ == "__main__":
    main()
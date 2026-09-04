import sqlite3
import pandas as pd

conn = None

try:
    conn = sqlite3.connect("../db/lesson.db")
    print("Database connected successfully.")

    query = """
    SELECT
        line_items.line_item_id,
        line_items.quantity,
        line_items.product_id,
        products.product_name,
        products.price
    FROM line_items
    JOIN products
    ON line_items.product_id = products.product_id
    """

    df = pd.read_sql_query(query, conn)

    print(df.head())

    df["total"] = df["quantity"] * df["price"]

    print("\nWith Total Column:")
    print(df.head())

    summary_df = df.groupby("product_id").agg({
        "line_item_id": "count",
        "total": "sum",
        "product_name": "first"
    })

    print("\nProduct Summary:")
    print(summary_df.head())

    summary_df = summary_df.sort_values("product_name")

    print("\nProduct Summary Sorted by Name:")
    print(summary_df.head())

    summary_df.to_csv("order_summary.csv")

except (sqlite3.Error, pd.errors.DatabaseError) as e:
    print("Database error:", e)

finally:
    if conn:
        conn.close()
        print("Database connection closed.")
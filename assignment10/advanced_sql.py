import sqlite3

conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

# Task 1: Complex JOINs with Aggregation
query = """
SELECT orders.order_id,
       SUM(products.price * line_items.quantity) AS total_price
FROM orders
JOIN line_items
ON orders.order_id = line_items.order_id
JOIN products
ON line_items.product_id = products.product_id
GROUP BY orders.order_id
ORDER BY orders.order_id
LIMIT 5;
"""

cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(row[0], row[1])



# Task 2: Subqueries
query2 = """
SELECT customers.customer_name,
       AVG(order_totals.total_price) AS average_total_price
FROM customers
LEFT JOIN (
    SELECT orders.customer_id AS customer_id_b,
           orders.order_id,
           SUM(products.price * line_items.quantity) AS total_price
    FROM orders
    JOIN line_items
    ON orders.order_id = line_items.order_id
    JOIN products
    ON line_items.product_id = products.product_id
    GROUP BY orders.order_id, orders.customer_id
) AS order_totals
ON customers.customer_id = order_totals.customer_id_b
GROUP BY customers.customer_id, customers.customer_name;
"""

cursor.execute(query2)
results2 = cursor.fetchall()

for row in results2:
    print(row[0], row[1])

# Task 3: Transactions and Inserts

try:
    
    cursor.execute("""
        SELECT customer_id
        FROM customers
        WHERE customer_name = ?;
    """, ("Perez and Sons",))

    customer_id = cursor.fetchone()[0]

    cursor.execute("""
        SELECT employee_id
        FROM employees
        WHERE first_name = ?
        AND last_name = ?;
    """, ("Miranda", "Harris"))

    employee_id = cursor.fetchone()[0]

    cursor.execute("""
        SELECT product_id
        FROM products
        ORDER BY price
        LIMIT 5;
    """)

    product_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("""
        INSERT INTO orders (customer_id, employee_id)
        VALUES (?, ?)
        RETURNING order_id;
    """, (customer_id, employee_id))

    order_id = cursor.fetchone()[0]

    for product_id in product_ids:
        cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, ?);
        """, (order_id, product_id, 10))

    conn.commit()

    cursor.execute("""
        SELECT line_items.line_item_id,
               line_items.quantity,
               products.product_name
        FROM line_items
        JOIN products
        ON line_items.product_id = products.product_id
        WHERE line_items.order_id = ?;
    """, (order_id,))

    task3_results = cursor.fetchall()

    for row in task3_results:
        print(row[0], row[1], row[2])

except Exception as e:
    conn.rollback()
    print("Transaction failed:", e)

# Task 4: GROUP BY and HAVING
query4 = """
SELECT employees.employee_id,
       employees.first_name,
       employees.last_name,
       COUNT(orders.order_id) AS order_count
FROM employees
JOIN orders
ON employees.employee_id = orders.employee_id
GROUP BY employees.employee_id,
         employees.first_name,
         employees.last_name
HAVING COUNT(orders.order_id) > 5;
"""

cursor.execute(query4)
results4 = cursor.fetchall()

for row in results4:
    print(row[0], row[1], row[2], row[3])

conn.close()
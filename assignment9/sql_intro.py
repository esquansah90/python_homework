
import sqlite3

conn = None

def add_publisher(cursor, name):
    try:
        cursor.execute(
            "INSERT INTO publishers (name) VALUES (?)",
            (name,)
        )
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")

def add_magazine(cursor, name, publisher_name):
    try:
        cursor.execute(
            "SELECT publisher_id FROM publishers WHERE name = ?",
            (publisher_name,)
        )

        result = cursor.fetchone()

        if result:
            publisher_id = result[0]

            cursor.execute(
                "INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",
                (name, publisher_id)
            )
        else:
            print(f"Publisher '{publisher_name}' does not exist.")

    except sqlite3.IntegrityError:
        print(f"Magazine '{name}' already exists.")

def add_subscriber(cursor, name, address):
    try:
        cursor.execute(
            """
            SELECT subscriber_id
            FROM subscribers
            WHERE name = ? AND address = ?
            """,
            (name, address)
        )

        result = cursor.fetchone()

        if result:
            print(f"Subscriber '{name}' at '{address}' already exists.")
        else:
            cursor.execute(
                """
                INSERT INTO subscribers (name, address)
                VALUES (?, ?)
                """,
                (name, address)
            )

    except sqlite3.Error as e:
        print("Error adding subscriber:", e)

def add_subscription(
    cursor,
    subscriber_name,
    subscriber_address,
    magazine_name,
    expiration_date
):
    try:
        cursor.execute(
            """
            SELECT subscriber_id
            FROM subscribers
            WHERE name = ? AND address = ?
            """,
            (subscriber_name, subscriber_address)
        )

        subscriber_result = cursor.fetchone()

        cursor.execute(
            """
            SELECT magazine_id
            FROM magazines
            WHERE name = ?
            """,
            (magazine_name,)
        )

        magazine_result = cursor.fetchone()

        if subscriber_result is None:
            print(f"Subscriber '{subscriber_name}' does not exist.")
            return

        if magazine_result is None:
            print(f"Magazine '{magazine_name}' does not exist.")
            return

        subscriber_id = subscriber_result[0]
        magazine_id = magazine_result[0]

        cursor.execute(
            """
            SELECT subscription_id
            FROM subscriptions
            WHERE subscriber_id = ? AND magazine_id = ?
            """,
            (subscriber_id, magazine_id)
        )

        existing_subscription = cursor.fetchone()

        if existing_subscription:
            print(
                f"{subscriber_name} is already subscribed "
                f"to '{magazine_name}'."
            )
        else:
            cursor.execute(
                """
                INSERT INTO subscriptions
                (subscriber_id, magazine_id, expiration_date)
                VALUES (?, ?, ?)
                """,
                (subscriber_id, magazine_id, expiration_date)
            )

    except sqlite3.Error as e:
        print("Error adding subscription:", e)

try:
    conn = sqlite3.connect("../db/magazines.db")
    print("Database connected successfully.")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
    )
    """)
    print("Tables created successfully.")

    add_publisher(cursor, "Penguin")
    add_publisher(cursor, "National Geographic")
    add_publisher(cursor, "Time")

    conn.commit()

    print("Publishers added successfully.")

    add_magazine(cursor, "Astronomy Magazine", "Time")
    add_magazine(cursor, "History Today", "Penguin")
    add_magazine(cursor, "National Geographic", "National Geographic")
    add_magazine(cursor, "Scientific American", "Time")
    add_magazine(cursor, "Biblical Archaeology", "Penguin")

    conn.commit()

    print("Magazines added successfully.")

    add_subscriber(cursor, "Sarah Ogoe", "123 Main Street")
    add_subscriber(cursor, "Stefano Brown", "456 Oak Avenue")
    add_subscriber(cursor, "Josiah Davis", "789 Pine Road")
    add_subscriber(cursor, "Emily Johnson", "321 Elm Street")
    add_subscriber(cursor, "Michael Smith", "654 Maple Lane")

    conn.commit()

    print("Subscribers added successfully.")

    add_subscription(
        cursor,
        "Sarah Ogoe",
        "123 Main Street",
        "National Geographic",
        "2027-08-29")

    add_subscription(
        cursor,
        "Stefano Brown",
        "456 Oak Avenue",
        "Scientific American",
        "2027-06-15")

    add_subscription(
        cursor,
        "Josiah Davis",
        "789 Pine Road",
        "Astronomy Magazine",
        "2027-12-01")

    conn.commit()
    print("Subscriptions added successfully.")

    cursor.execute("SELECT * FROM subscribers")

    subscribers = cursor.fetchall()

    print("\nAll Subscribers:")

    for subscriber in subscribers:
        print(subscriber)

    cursor.execute("""
        SELECT *
        FROM magazines
        ORDER BY name
    """)

    magazines = cursor.fetchall()

    print("\nAll Magazines Sorted by Name:")

    for magazine in magazines:
        print(magazine)

    cursor.execute("""
        SELECT magazines.name, publishers.name
        FROM magazines
        JOIN publishers
        ON magazines.publisher_id = publishers.publisher_id
        WHERE publishers.name = ?
    """, ("Penguin",))

    publisher_magazines = cursor.fetchall()

    print("\nMagazines Published by Penguin:")

    for magazine in publisher_magazines:
        print(magazine)

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if conn:
        conn.close()
        print("Database connection closed.")
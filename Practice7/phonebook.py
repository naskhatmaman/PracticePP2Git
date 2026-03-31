import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host="localhost",
        database="phonebook_db",
        user="postgres",
        password="1234",
        port=5432
    )

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20) UNIQUE
        );
        """)
    conn.commit()

def insert_from_csv(conn):
    with open("contacts.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = [(row['name'], row['phone']) for row in reader]

    with conn.cursor() as cur:
        cur.executemany(
            "INSERT INTO phonebook (name, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING",
            data
        )
    conn.commit()
    print("CSV inserted!")

def insert_console(conn):
    name = input("Name: ")
    phone = input("Phone: ")

    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
            (name, phone)
        )
    conn.commit()

def show_all(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM phonebook")
        rows = cur.fetchall()
        print("\nID   Name        Phone")
        print("---------------------------")
        for r in rows:
            print(r)

def update(conn):
    phone = input("Enter phone: ")
    new_name = input("New name: ")

    with conn.cursor() as cur:
        cur.execute(
            "UPDATE phonebook SET name=%s WHERE phone=%s",
            (new_name, phone)
        )
    conn.commit()

def delete(conn):
    phone = input("Enter phone: ")

    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM phonebook WHERE phone=%s",
            (phone,)
        )
    conn.commit()

def main():
    conn = connect()
    create_table(conn)

    while True:
        print("\n1. Import CSV")
        print("2. Add")
        print("3. Show")
        print("4. Update")
        print("5. Delete")
        print("0. Exit")

        ch = input("Choose: ")

        if ch == "1":
            insert_from_csv(conn)
        elif ch == "2":
            insert_console(conn)
        elif ch == "3":
            show_all(conn)
        elif ch == "4":
            update(conn)
        elif ch == "5":
            delete(conn)
        elif ch == "0":
            break

    conn.close()

main()
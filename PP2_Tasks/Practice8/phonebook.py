import csv
from connect import open_connection


def create_phonebook_table():
    sql = """
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20) UNIQUE
    );
    """

    conn = open_connection()
    cur = conn.cursor()

    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()

    print("Table created.")


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = open_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
    conn.commit()

    cur.close()
    conn.close()

    print("Done.")


def load_from_csv():
    import os
    import csv
    from connect import open_connection

    file_path = os.path.join(os.path.dirname(__file__), "contacts.csv")

    conn = open_connection()
    cur = conn.cursor()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            rows = list(reader)

            if len(rows) <= 1:
                print("CSV is empty")
                return

            for row in rows[1:]:
                name, phone = row
                cur.execute(
                    "CALL upsert_contact(%s, %s);",
                    (name, phone)
                )

        conn.commit()
        print("CSV loaded.")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    cur.close()
    conn.close()


def search():
    text = input("Enter search text: ")

    conn = open_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s);", (text,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def show_paginated():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    conn = open_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete_contact():
    name = input("Enter name (or leave empty): ")
    phone = input("Enter phone (or leave empty): ")

    conn = open_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s, %s);", (name if name else None, phone if phone else None))
    conn.commit()

    cur.close()
    conn.close()

    print("Deleted.")


def menu():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Create table")
        print("2. Add contact (upsert)")
        print("3. Load from CSV")
        print("4. Search")
        print("5. Show paginated")
        print("6. Delete")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            create_phonebook_table()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            load_from_csv()
        elif choice == "4":
            search()
        elif choice == "5":
            show_paginated()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            break
        else:
            print("Invalid choice")


menu()
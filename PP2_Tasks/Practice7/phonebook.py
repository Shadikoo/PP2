import csv
from connect import open_connection


# ✅ CREATE TABLE
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


# ✅ INSERT FROM CONSOLE
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    sql = "INSERT INTO contacts (name, phone) VALUES (%s, %s);"

    conn = open_connection()
    cur = conn.cursor()

    try:
        cur.execute(sql, (name, phone))
        conn.commit()
        print("Contact added.")
    except Exception as e:
        conn.rollback()
        print("Error:", e)

    cur.close()
    conn.close()


# ✅ INSERT FROM CSV
def load_from_csv():
    conn = open_connection()
    cur = conn.cursor()

    try:
        with open("contacts.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                name, phone = row
                cur.execute(
                    "INSERT INTO contacts (name, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING;",
                    (name, phone)
                )

        conn.commit()
        print("CSV loaded.")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    cur.close()
    conn.close()


# ✅ SELECT
def show_contacts():
    conn = open_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts;")
    data = cur.fetchall()

    if not data:
        print("No contacts found.")
    else:
        for row in data:
            print(row)

    cur.close()
    conn.close()


# ✅ SEARCH BY NAME
def search_by_name():
    name = input("Enter name to search: ")

    conn = open_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE name ILIKE %s;",
        (f"%{name}%",)
    )

    results = cur.fetchall()

    for row in results:
        print(row)

    if not results:
        print("No matches.")

    cur.close()
    conn.close()


# ✅ SEARCH BY PHONE PREFIX
def search_by_phone():
    prefix = input("Enter phone prefix: ")

    conn = open_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE phone LIKE %s;",
        (f"{prefix}%",)
    )

    results = cur.fetchall()

    for row in results:
        print(row)

    if not results:
        print("No matches.")

    cur.close()
    conn.close()


# ✅ UPDATE (NAME OR PHONE)
def edit_contact():
    print("1. Change name")
    print("2. Change phone")

    choice = input("Choose option: ")

    conn = open_connection()
    cur = conn.cursor()

    try:
        if choice == "1":
            phone = input("Enter phone: ")
            new_name = input("Enter new name: ")

            cur.execute(
                "UPDATE contacts SET name = %s WHERE phone = %s;",
                (new_name, phone)
            )

        elif choice == "2":
            name = input("Enter name: ")
            new_phone = input("Enter new phone: ")

            cur.execute(
                "UPDATE contacts SET phone = %s WHERE name = %s;",
                (new_phone, name)
            )

        else:
            print("Wrong choice")
            return

        conn.commit()

        if cur.rowcount == 0:
            print("No contact found.")
        else:
            print("Contact updated.")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    cur.close()
    conn.close()


# ✅ DELETE
def remove_contact():
    print("1. Delete by name")
    print("2. Delete by phone")

    choice = input("Choose option: ")

    conn = open_connection()
    cur = conn.cursor()

    try:
        if choice == "1":
            name = input("Enter name: ")
            cur.execute("DELETE FROM contacts WHERE name = %s;", (name,))

        elif choice == "2":
            phone = input("Enter phone: ")
            cur.execute("DELETE FROM contacts WHERE phone = %s;", (phone,))

        else:
            print("Wrong choice")
            return

        conn.commit()

        if cur.rowcount == 0:
            print("No contact found.")
        else:
            print("Contact deleted.")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    cur.close()
    conn.close()


# ✅ MENU
def menu():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Create table")
        print("2. Add contact")
        print("3. Load from CSV")
        print("4. Show all contacts")
        print("5. Search by name")
        print("6. Search by phone prefix")
        print("7. Update contact")
        print("8. Delete contact")
        print("9. Exit")

        choice = input("Choose: ")

        if choice == "1":
            create_phonebook_table()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            load_from_csv()
        elif choice == "4":
            show_contacts()
        elif choice == "5":
            search_by_name()
        elif choice == "6":
            search_by_phone()
        elif choice == "7":
            edit_contact()
        elif choice == "8":
            remove_contact()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


# 🚀 RUN
menu()
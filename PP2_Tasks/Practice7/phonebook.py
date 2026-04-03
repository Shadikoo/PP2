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

    sql = "INSERT INTO contacts (name, phone) VALUES (%s, %s);"

    conn = open_connection()
    cur = conn.cursor()

    cur.execute(sql, (name, phone))
    conn.commit()

    cur.close()
    conn.close()

    print("Contact added.")


def load_from_csv():
    conn = open_connection()
    cur = conn.cursor()

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
    cur.close()
    conn.close()

    print("CSV loaded.")


def show_contacts():
    conn = open_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts;")
    data = cur.fetchall()

    for row in data:
        print(row)

    cur.close()
    conn.close()


def edit_contact():
    old_phone = input("Enter phone to update: ")
    new_name = input("New name: ")

    conn = open_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE contacts SET name = %s WHERE phone = %s;",
        (new_name, old_phone)
    )

    conn.commit()

    cur.close()
    conn.close()

    print("Updated.")


def remove_contact():
    phone = input("Enter phone to delete: ")

    conn = open_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM contacts WHERE phone = %s;", (phone,))
    conn.commit()

    cur.close()
    conn.close()

    print("Deleted.")


def menu():
    while True:
        print("\n1.Create table")
        print("2.Add contact")
        print("3.Load CSV")
        print("4.Show contacts")
        print("5.Update contact")
        print("6.Delete contact")
        print("7.Exit")

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
            edit_contact()
        elif choice == "6":
            remove_contact()
        elif choice == "7":
            break


menu()
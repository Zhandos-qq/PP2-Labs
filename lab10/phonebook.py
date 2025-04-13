import psycopg2
import csv

conn = psycopg2.connect( # creating a connection
   database="postgres",
    user="postgres",
    host="localhost",
    password="1234",
    port=5432
)

# Creating table if it doesn't exist
def create_table():

# Check if the table already exists
    command = "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'phonebook')"
    with conn.cursor() as cur:
        cur.execute(command)
        exists = cur.fetchone()[0]

    if exists:
        print("Table already exists.")
        return
    
    command = """CREATE TABLE phonebook (
                id SERIAL PRIMARY KEY,
                user_name VARCHAR(255),
                phone VARCHAR(12)
            )"""
    

    with conn.cursor() as cur:
        # execute the command
        cur.execute(command)
        conn.commit()
        
    ch = input("Table created successfully. Press Enter to continue...")
    return ch

# Delete table if it exists
def drop_table():
    command = "DROP TABLE IF EXISTS phonebook"

    with conn.cursor() as cur:
        # execute the command
        cur.execute(command)
        conn.commit()



# Insert user by terminal
def insert(user_name, phone):

    command = "INSERT INTO phonebook(user_name, phone) VALUES(%s, %s)"

    with conn.cursor() as cur:
        # execute the command
        cur.execute(command, (user_name, phone))
        conn.commit()

# Insert from csv file
def insert_from_csv(csv_file_name):

    command = "INSERT INTO phonebook(user_name, phone) VALUES(%s, %s)"

    with conn.cursor() as cur:
        # execute the command
        with open(csv_file_name, "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            _ = next(csvreader) # getting rid of the headers
            for row in csvreader:
                user_name, phone = row
                cur.execute(command, (user_name, phone))
        conn.commit()



# Get names filter by first letter
def get_names_filter_by_letter(letter):
    command = "SELECT * FROM phonebook WHERE user_name LIKE %s"
    with conn.cursor() as cur:
        cur.execute(command, (letter,)) # (,) is to show that we have a tuple
        results = cur.fetchall()
        if not results:
            print("No users found starting with that letter.")
        else:
            for row in results:
                print(row)

# Get names filter by provider
def get_names_filter_by_provider(provider):
    provider_prefixes = {
        'kcell': ['701', '702', '775', '778'],
        'beeline': ['705', '777'],
        'tele2': ['707', '747'],
        'altel': ['708', '709', '770', '700'],
    }

    prefixes = provider_prefixes.get(provider.lower())
    if not prefixes:
        print("Unknown provider.")
        return

    with conn.cursor() as cur:
        results = []
        for prefix in prefixes:
            # проверяем и номера с +7 и с 8
            cur.execute("""
                SELECT * FROM phonebook 
                WHERE phone LIKE %s OR phone LIKE %s
            """, (f'+7{prefix}%', f'8{prefix}%'))
            results += cur.fetchall()
        
        if not results:
            print("No entries found for this provider.")
        else:
            for row in results:
                print(row)


        
# Update name
def update_user_name():
    # current_name = input("Enter current user name: ")
    current_phone = input("Enter current phone number: ")
    new_name = input("Enter new user name: ")

    command = "UPDATE phonebook SET user_name = %s WHERE phone = %s"
    with conn.cursor() as cur:
        cur.execute(command, (new_name, current_phone))
        if cur.rowcount == 0:
            print("No matching user found.")
        else:
            print("User name updated successfully.")
        conn.commit()

# Update phone number
def update_user_phone():
    # current_name = input("Enter current user name: ")
    current_phone = input("Enter current phone number: ")
    new_phone = input("Enter new phone number: ")

    command = "UPDATE phonebook SET phone = %s WHERE phone = %s"
    with conn.cursor() as cur:
        cur.execute(command, (new_phone, current_phone))
        if cur.rowcount == 0:
            print("No matching user found.")
        else:
            print("Phone number updated successfully.")
        conn.commit()



# DELETE USER
def delete_user(phone):
   
    command = "DELETE FROM phonebook WHERE phone = %s"

    with conn.cursor() as cur:
        cur.execute(command, (phone,))
        conn.commit()

#Select all users
def select_all():
    command = "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'phonebook')"
    with conn.cursor() as cur:
        cur.execute(command)
        exists = cur.fetchone()[0]
    if exists:
        command = "SELECT * FROM phonebook"
    else:
        print("Table does not exist.")
        # return empty list if table does not exist
        return

    with conn.cursor() as cur:
        cur.execute(command)
        return cur.fetchall()


import sqlite3

def run_sql_command(command):
    # Connect to the SQLite database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    try:
        # Execute the command
        cursor.execute(command)
        
        # If the command is a "SELECT" query, fetch the results
        if command.strip().upper().startswith('SELECT'):
            results = cursor.fetchall()
            for row in results:
                print(row)
        else:
            # Commit changes for non-query commands (like INSERT, UPDATE, DELETE)
            conn.commit()
            print("Command executed successfully.")
    except sqlite3.Error as e:
        print("An error occurred:", e)
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

# Main program loop
def main():
    while True:
        print("\nSQLite Interactive Command Runner")
        command = input("Enter an SQLite command or 'exit' to quit: ")
        
        if command.lower() == 'exit':
            print("Exiting the interactive runner.")
            break
        else:
            run_sql_command(command)

if __name__ == '__main__':
    main()



# import sqlite3

# # Connect to the database
# conn = sqlite3.connect('example.db')

# # Create a cursor object
# cur = conn.cursor()

# # Create a table
# cur.execute('''CREATE TABLE IF NOT EXISTS stocks
#                (date text, trans text, symbol text, qty real, price real)''')

# # Insert a row of data
# cur.execute("INSERT INTO stocks VALUES ('2022-01-05','BUY','RHAT',100,35.14)")

# # Save (commit) the changes
# conn.commit()

# # Query the database
# cur.execute("SELECT * FROM stocks WHERE trans='BUY'")
# print(cur.fetchall())

# # Close the connection
# cur.close()
# conn.close()

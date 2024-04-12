#!/usr/bin/python3

import MySQLdb

def list_states_with_n(username, password, database):
    """
    Connects to the MySQL server and lists all states with a name starting with 'N' from the specified database.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database to connect to.

    Returns:
        None
    """
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                )

        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Execute the query to retrieve states starting with 'N'
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

        # Fetch all rows
        states = cursor.fetchall()

        # Display the states
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    import sys

    # Check if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Retrieve arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to list states starting with 'N'
    list_states_with_n(username, password, database)


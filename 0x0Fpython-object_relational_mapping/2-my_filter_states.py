#!/usr/bin/python3
import MySQLdb

def search_states(username, password, database, state_name):
    """
    Connects to the MySQL server and searches for states with the specified name in the specified database.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database to connect to.
        state_name (str): The name of the state to search for.

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

        # Execute the query to search for states with the specified name
        query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
        cursor.execute(query, (state_name,))

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
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    # Retrieve arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to search for states
    search_states(username, password, database, state_name)

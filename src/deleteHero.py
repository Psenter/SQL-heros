import psycopg2
from psycopg2 import OperationalError
from database.connection import execute_query, create_connection

def deleteHero():
    name = input("What is the name of the hero you want to remove? ")

    try:
        connection = create_connection("postgres", "postgres", "postgres")
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM heroes WHERE name = %s", (name,))
        count = cursor.fetchone()[0]

        if count == 0:
            print(f"Hero is not found in the database.")
        else:
            query = "DELETE FROM heroes WHERE name = %s"
            params = (name,)

            cursor.execute(query, params)
            connection.commit()
            print("Successfully deleted the hero.")
    except OperationalError as e:
        print("The error '{e}' occurred.")
    finally:
        cursor.close()
        connection.close()

deleteHero()
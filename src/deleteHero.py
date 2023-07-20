import psycopg2
from database.connection import execute_query, create_connection

def delete_hero():
    name = input("Enter the name of the hero you would like to remove: ")
    query = "DELETE FROM heroes WHERE name = %s"
    params = (name,)

    try:
        execute_query(query, params)
        print(f"Successfully deleted the hero.")
    except psycopg2.Error as e:
        print(f"Error occurred while deleting the hero: {e}")

delete_hero()
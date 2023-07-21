#the comma after things like (name,) turns it into a string

import psycopg2
from psycopg2 import OperationalError
from database.connection import execute_query, create_connection

def deleteHero():

    #gets the name of the hero the user wants to delete
    name = input("What is the name of the hero you want to remove? ")

    try:
        connection = create_connection("postgres", "postgres", "postgres")
        cursor = connection.cursor()

        #checks if the entered name exists in the table and stores the ID in the fetchone() method
        cursor.execute("SELECT COUNT(*) FROM heroes WHERE name = %s", (name,))
        count = cursor.fetchone()[0]

        #checks if the count is 0, if it is then there is no hero with that name in the database
        if count == 0:
            print(f"Hero is not found in the database.")

        #if the count is above 0 it deletes the hero from the database
        else:
            #constructs the query to delete the hero from the database
            query = "DELETE FROM heroes WHERE name = %s"
            params = (name,)

            #uses the cursor connection made before to delete the hero
            cursor.execute(query, params)
            #commits the changes made
            connection.commit()
            #prints message to the console saying the hero was deleted
            print("Successfully deleted the hero.")

    #if an error occurs then this message is displayed
    except OperationalError as e:
        print("The error '{e}' occurred.")

    #closes connection to the database
    finally:
        connection.close()

deleteHero()
#fetchone() fetchs all rows and looks over them
#is similar to fetch all
#get more in depth answer about it 

import psycopg2
from database.connection import execute_query, create_connection

def createHero():

    #Prompts user to put in input and stores the input
    name = input("What is your hero's name? ")
    aboutMe = input("Give a short description about your hero: ")
    biography = input("What's your hero's backstory? ")
    superpower = input("What superpower does your hero have? ")

    #Creates the connection to the database
    connection = create_connection("postgres", "postgres", "postgres")

    #checks if the connection to database was successful 
    #if connection fails skips the try block and executes the except block
    if connection:
        try:
            with connection:

                #creates a cursor object that lets SQL queries be made
                with connection.cursor() as cursor:
                    
                    #checks if the user input superpower already exists within the abilities table
                    cursor.execute("SELECT id FROM ability_types WHERE name = %s", (superpower,))
                    existing_superpower_id = cursor.fetchone()

                    #if the superpower already exists it gets the ID of that power and stores it
                    if existing_superpower_id:
                        superpower_id = existing_superpower_id[0]
                    
                    #if the power does not exist then it makes a new addition to the table and gives it an unique ID
                    else:
                        cursor.execute("INSERT INTO ability_types (name) VALUES (%s) RETURNING id", (superpower,))
                        superpower_id = cursor.fetchone()[0]

                    #adds the hero and everything that goes with it to the respective table and gives the hero a unique ID
                    query = "INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s) RETURNING id"
                    params = (name, aboutMe, biography)
                    cursor.execute(query, params)
                    hero_id = cursor.fetchone()[0]

                    #adds the new superpower to the respective table and the new ID made for it
                    ability_query = "INSERT INTO abilities (hero_id, ability_type_id) VALUES (%s, %s)"
                    ability_params = (hero_id, superpower_id)
                    cursor.execute(ability_query, ability_params)

            #prints this to console if creating the new hero was successful
            print("You've successfully created your hero!")

        #if an error occured this is displayed in console
        except psycopg2.Error as e:
            print("Error creating the hero:", e)
        
        #closes the connection to the database at the end no matter what happened
        finally:
            connection.close()

#calls the function to be ran
createHero()
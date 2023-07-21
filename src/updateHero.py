import psycopg2
from database.connection import execute_query, create_connection

def updateHero():
    connection = create_connection("postgres", "postgres", "postgres")
    if connection:
        try:
            with connection:
                with connection.cursor() as cursor:
                    
                    #gets the names and ids from all the heros 
                    cursor.execute("SELECT id, name FROM heroes")
                    heroes = cursor.fetchall()

                    #prints a list of all the heros into the console
                    print("List of existing heroes:")
                    for hero in heroes:
                        print(f"{hero[0]}. {hero[1]}")

                    #while true loop, keeps loop running until its true
                    while True:
                        heroChoice = input("Enter the name of the hero you want to update: ")
                        try:

                            #trys to turn the user input into a integer
                            heroChoice = int(heroChoice)

                            #if the hero name/ID entered is not in the database the error is displayed
                            #if it is in the database the code breaks and continues to the next part
                            if heroChoice not in [hero[0] for hero in heroes]:
                                raise ValueError("Invalid hero. Please choose a name.")
                            break

                        #if the code runs into a value error then it goes through this code block
                        #when this happens it means the user did not put in an integer
                        except ValueError:

                            #sets the hero ID to none
                            #will be used to store the hero ID if a name is found
                            heroId = None

                            #iterates through all the heros in the table
                            for hero in heroes:

                                #checks if the entered name matches any in the database
                                #if one is found then it breaks the loop
                                if heroChoice == hero[1]:
                                    heroId = hero[0]
                                    break

                            #find the corresponding ID to the name then breaks loop
                            if heroId:
                                heroChoice = heroId
                                break

                            #if nothing is successful this error message is displayed
                            print("Invalid hero name. Please choose a valid ID or name.")

                    #retrevies all the information on the current hero selected
                    #stores everything in the heroInfo varaible 
                    cursor.execute("SELECT name, about_me, biography FROM heroes WHERE id = %s", (heroChoice,))
                    heroInfo = cursor.fetchone()

                    #prints all of the hero information for the user to see
                    #f makes it a string literal (like a template literal from JS)
                    #\n is for a new line
                    #{} <- vars inside of the braces are the hero and all the data from the table
                    print(f"\nCurrent Hero Information (ID: {heroChoice}):")
                    print(f"Name: {heroInfo[0]}")
                    print(f"About Me: {heroInfo[1]}")
                    print(f"Biography: {heroInfo[2]}")

                    #asks the user what they would like to update in the information
                    updatedName = input("Enter the updated name (or leave empty to keep current): ")
                    updatedAboutMe = input("Enter the updated short description: ")
                    updatedBiography = input("Enter the updated backstory: ")
                    updatedSuperPower = input("Enter the updated superpower: ")

                    #checks if any of the above input fields have text in them
                    if updatedName or updatedAboutMe or updatedBiography or updatedSuperPower:

                        #if there was something typed into an input it will update the table with the new information
                        update_query = "UPDATE heroes SET name = COALESCE(%s, name), about_me = COALESCE(%s, about_me), biography = COALESCE(%s, biography) WHERE id = %s"
                        update_params = (updatedName, updatedAboutMe, updatedBiography, heroChoice)
                        cursor.execute(update_query, update_params)

                        #after updating the above information it moves on to updating the powers
                        #checks if the power already exists
                        cursor.execute("SELECT id FROM ability_types WHERE name = %s", (updatedSuperPower,))
                        existing_superpower_id = cursor.fetchone()

                        #if the superpower exists them it sets its ID to the existing
                        if existing_superpower_id:
                            superpower_id = existing_superpower_id[0]

                        #if it does not exist it creates a new power with a new ID
                        else:
                            cursor.execute("INSERT INTO ability_types (name) VALUES (%s) RETURNING id", (updatedSuperPower,))
                            superpower_id = cursor.fetchone()[0]

                        #updates the abilities table with the new powers for that hero
                        update_ability_query = "UPDATE abilities SET ability_type_id = %s WHERE heroId = %s"
                        update_ability_params = (superpower_id, heroChoice)
                        cursor.execute(update_ability_query, update_ability_params)

                        #prints that the changes were made to the console
                        print("Hero information updated successfully!")

                    #if all input fields are blank it displays this message to the console showing nothing was changed about the hero
                    else:
                        print("No updates made. Hero information remains unchanged.")

        #if an error occurs then this message is displayed
        except psycopg2.Error as e:
            print("Error updating the hero:", e)

        #closes connection with database
        finally:
            connection.close()

updateHero()
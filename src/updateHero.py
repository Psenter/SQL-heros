import psycopg2
from database.connection import execute_query, create_connection

def updateHero():
    connection = create_connection("postgres", "postgres", "postgres")
    if connection:
        try:
            with connection:
                with connection.cursor() as cursor:

                    cursor.execute("SELECT id, name FROM heroes")
                    heroes = cursor.fetchall()

                    print("List of existing heroes:")
                    for hero in heroes:
                        print(f"{hero[0]}. {hero[1]}")

                    while True:
                        heroChoice = input("Enter the name of the hero you want to update: ")
                        try:
                            heroChoice = int(heroChoice)
                            if heroChoice not in [hero[0] for hero in heroes]:
                                raise ValueError("Invalid hero. Please choose a name.")
                            break
                        except ValueError:
                            heroId = None
                            for hero in heroes:
                                if heroChoice == hero[1]:
                                    heroId = hero[0]
                                    break
                            if heroId:
                                heroChoice = heroId
                                break
                            print("Invalid hero name. Please choose a valid ID or name.")

                    cursor.execute("SELECT name, about_me, biography FROM heroes WHERE id = %s", (heroChoice,))
                    heroInfo = cursor.fetchone()

                    print(f"\nCurrent Hero Information (ID: {heroChoice}):")
                    print(f"Name: {heroInfo[0]}")
                    print(f"About Me: {heroInfo[1]}")
                    print(f"Biography: {heroInfo[2]}")

                    updatedName = input("Enter the updated name (or leave empty to keep current): ")
                    updatedAboutMe = input("Enter the updated short description: ")
                    updatedBiography = input("Enter the updated backstory: ")
                    updatedSuperPower = input("Enter the updated superpower: ")

                    if updatedName or updatedAboutMe or updatedBiography or updatedSuperPower:
                        update_query = "UPDATE heroes SET name = COALESCE(%s, name), about_me = COALESCE(%s, about_me), biography = COALESCE(%s, biography) WHERE id = %s"
                        update_params = (updatedName, updatedAboutMe, updatedBiography, heroChoice)
                        cursor.execute(update_query, update_params)

                        cursor.execute("SELECT id FROM ability_types WHERE name = %s", (updatedSuperPower,))
                        existing_superpower_id = cursor.fetchone()

                        if existing_superpower_id:
                            superpower_id = existing_superpower_id[0]
                        else:
                            cursor.execute("INSERT INTO ability_types (name) VALUES (%s) RETURNING id", (updatedSuperPower,))
                            superpower_id = cursor.fetchone()[0]

                        update_ability_query = "UPDATE abilities SET ability_type_id = %s WHERE heroId = %s"
                        update_ability_params = (superpower_id, heroChoice)
                        cursor.execute(update_ability_query, update_ability_params)

                        print("Hero information updated successfully!")
                    else:
                        print("No updates made. Hero information remains unchanged.")

        except psycopg2.Error as e:
            print("Error updating the hero:", e)
        finally:
            connection.close()

updateHero()
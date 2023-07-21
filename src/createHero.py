import psycopg2
from database.connection import execute_query, create_connection

def create_hero():
    name = input("What is your hero's name? ")
    aboutMe = input("Give a short description about your hero: ")
    biography = input("What's your hero's backstory? ")

    superpower = input("What superpower does your hero have? ")

    connection = create_connection("postgres", "postgres", "postgres")

    if connection:
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT id FROM ability_types WHERE name = %s", (superpower,))
                    existing_superpower_id = cursor.fetchone()

                    if existing_superpower_id:
                        superpower_id = existing_superpower_id[0]
                    else:
                        cursor.execute("INSERT INTO ability_types (name) VALUES (%s) RETURNING id", (superpower,))
                        superpower_id = cursor.fetchone()[0]

                    query = "INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s) RETURNING id"
                    params = (name, aboutMe, biography)
                    cursor.execute(query, params)

                    hero_id = cursor.fetchone()[0]

                    ability_query = "INSERT INTO abilities (hero_id, ability_type_id) VALUES (%s, %s)"
                    ability_params = (hero_id, superpower_id)
                    cursor.execute(ability_query, ability_params)

            print("You've successfully created your hero!")
        except psycopg2.Error as e:
            print("Error creating the hero:", e)
        finally:
            connection.close()

create_hero()
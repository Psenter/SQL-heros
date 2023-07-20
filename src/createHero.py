import psycopg2
from database.connection import execute_query, create_connection

def create_hero():
    # Prompt the user for hero details
    name = input("What is your hero's name? ")
    about_me = input("Give a short description about your hero: ")
    biography = input("What's your hero's backstory? ")
    query = "INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s)"
    params = (name, about_me, biography)
    execute_query(query, params)
    print("You've successfully created your hero!")

create_hero()
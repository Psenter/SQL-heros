import psycopg2
from database.connection import execute_query, create_connection

def updateHero():
    updater = input("What hero would you like to update? ")

    updateName = input("Would you like to change this hero's name? ")
    # turn the input to lowercase
    #figure out how to pull the input for IF statements
    if input == "yes":
        changeHeroName = input("What would you like to change the hero's name to? ")
        return ("Hero's name has been changed.")

    updatePower = input("Would you like to change the power(s) of this hero? ")
    if input == "yes":
        changeHeroPower = input("What would you like to change the power(s) to? ")
        return ("The hero's power(s) have been changed.")
    
    updateBackStory = input("Would you like to change the hero's backstory?")
    if input == "yes":
        changeHeroBackStory = input("What would you like to change the backstory to? ")
        return ("The hero's backstory has been changed.")
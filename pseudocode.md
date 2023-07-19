<!-- Questions: -->
<!-- How to make the if else statements work as one string of questions instead of one question ending the function -->
<!-- How to get the answers to the questions to add, update, or remove things from the list -->

# MoSCoW
### Must have:
* Create new hero
* Read and display table with all the heros (including new one)
* Update new hero
* Delete a hero from the table
### Should have:
* Can add new friends
* Can add likes/dislikes
* Heros can have multiple abilities
### Could have:
* Can have mutual enemies
* Can add new enemies
* ASCII art for some visual elements
### Won't have:
* Front end work

# User stories
* As anonymous user, I want to be able to add new heros, so my own heros can be displayed
* As anonymous user, I want to be able to display the whole table, so that I can see all the heros together
* As anonymous user, I want to be able to update heros, so that if a story or ability changes I am able to display them
* As anonymous user, I want to be able to delete heros, so that if I do not want to continue their story or don't like them anymore they don't have to be displayed

# Procedural 
1. Create a connection to the database using python to be able to view it
2. Create the table and get the appropriate tables/entries created
3. Implement the CRUD operations (create, read, update, and delete)
4. Have the CRUD operations displayed in the table (creation, reading, updates, and deletion of any new or old heros)

# Functional and OOP
## CRUD:

### C:
```
def createHero():
    name = input("What's your hero's name?)
    superhero = input("What's your hero's superpower?")
    backstory = input("What's your hero's back story?)
    //add all input to respective tables (look into how to do that from input)
    return ("Your hero has been created.")
```

### R:
```
execute_query("SELECT * FROM heroes;")
```
(could do for select heros, abilities, etc.)

### U:
```
def updateHero():
    heroName = input("Do you want to change the hero's name?)
    if input == yes:
        changeName = input("What would you like the new name to be?")
        return ("Name has been changed.")
    else: //move onto the next question

    heroPower = input("Would you like to change the superpowers of this hero?)
    if input == yes:
        changePower = input("What would you like the new power(s) to be?")
        return ("Power has been changed.")
    else: //move onto the next question

    heroBackStory = input("Would you like to change the hero's back story?")
    if input == yes:
        changeBackStory = input("What would you like the new back story to be?")
        return ("Back story has been changed for this hero.")
    else: //end function
```

### D:
```
def deleteHero():
    name = input("What is the name of hero you would like to remove?")
    return ("Hero has been removed.")
```
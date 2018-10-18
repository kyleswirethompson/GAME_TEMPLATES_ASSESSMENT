#!/usr/bin/python3

from map import rooms
import string


def remove_punct(text):

    new_text = ""
    pass # The pass statement does nothing. Replace it with the body of your function.
    for i in text :
        if i not in  ["¬","£","!","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~",":"]:
            new_text = new_text + i
            
    return new_text

    
def remove_spaces(text):
    
    text = text.strip()
    
    return text


def normalise_input(user_input):
   
    user_input = remove_punct(user_input)    
    user_input = remove_spaces(user_input)
    
    return user_input.lower()

    
def display_room(room):

    print("")
    print(room["name"].upper())
    print("")
    print(room["description"])
    print("")

    
def exit_leads_to(exits, direction):
    
    room_direction_leads_to = exits[direction]    # converting the name into the correct format    
    leads_to = rooms[room_direction_leads_to]["name"]    
                  
    return leads_to
    

def print_menu_line(direction, leads_to):

    print("Go " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits):

    print("You can:")
    
    # COMPLETE THIS PART:
    # Iterate over available exits:
    #     and for each exit print the appropriate menu line

    for i in exits:        
        leads_to = exit_leads_to(exits, i)
        print_menu_line( i, leads_to)        
    print("Where do you want to go?")


def is_valid_exit(exits, user_input):

    if user_input in exits:
        return True
    else:
        return False
    
    pass


def menu(exits):

    # Repeat until the player enter a valid choice
    while True:
        # Display menu
        print_menu(exits)
        # Read player's input
        players_input = input("")
        # Normalise the input
        players_input = normalise_input(players_input)
        # Check if the input makes sense (is valid exit)   
            # If so, return the player's choice
        if is_valid_exit(exits, players_input) == True:
            
            return players_input


def move(exits, direction):
    
    new_room = exits[direction]
    new_room = rooms[new_room]
    
    return new_room


def main():
    
    # Start game at the reception
    current_room = rooms["Reception"]
    # Main game loop
    while True:
        # Display game status (room description etc.)
        display_room(current_room)
        # What are the possible exits from the current room?
        exits = current_room["exits"]
        # Show the menu with exits and ask the player
        direction = menu(exits)       
        # Move the protagonist, i.e. update the current room
        current_room = move(exits, direction)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

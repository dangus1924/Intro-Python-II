from room import Room
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

darren = Player(room['outside'])
current_room = room['outside']
print(current_room)
 
quit = False


while quit is False:
    print(f'Current Room: {darren.current_room}')
    print(f'Description: {current_room.description}')

    if current_room.name == 'Treasure Chamber':
        print('***** YOU HAVE FOUND THE TRESURE ROOM *****')

    command = input(
        '\n\nWhat is you next move? \n(E)xplore Current Room\n(G)o to new Room\n(Q)uit\n\n\n')
    if command == '':
        continue
    command = command.strip().lower()[0]
    if command == 'q':
        quit = True
    elif command == 'e':
        if not current_room.name:
            print('You will be able to find items in this room in the next update but not now cheater!!!!!!!!!')
    elif command == 'g':
        direction = input('\nWhich Direction whould you like to go?\n(n)orth\n(e)ast\n(s)outh\n(w)est\n(q)uit\n\n\n')
        while direction not in ('n', 's', 'e', 'w', 'q'):
            print('\n********* Please choose a valid direction, I made it easy look on the screen...... forget you lost!! \nJK keep going!')
            direction = input('\n Which Direction would you like to g?\n(n)orth\n(e)ast\n(s)outh\n(w)est\n(q)uit\n\n\n')
        if direction == 'q':
            quit = True
            continue
        direction = direction.strip().lower()[0] + '_to'
        print(f'Alright. we are going {direction}.')

        other_room = getattr(current_room, direction)
        
        if other_room is None:
            print("a room doesn't exist in that direction")
        else:
            current_room = darren.current_room = other_room
            print(f"darren's current room: {darren.current_room}")
    
    

        

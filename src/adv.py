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


print(f'''                                     
                                            The Game of Adventure
''')
user_name = input("What is your name ? ")

print(
    f''' 
                                             Welcome {user_name}  😊
    '''
)
player = Player(user_name, room['outside'])

game_on = True
while game_on:

    print(f'''
    [N]for North 👆   
    [S] for South 👇  
    [E] for East 👉 
    [W] for West 👈 
    [Q] to Quit 🙁

    Now, you are at the {player.current_room.name} room
    ''')

    user_direction = input("Next move ? ").upper()

    # North
    if user_direction == "N":
        next_move = player.current_room.n_to
        if next_move == None:
            print("You are block, try picking different road")
        else:
            player.current_room = next_move

# South
    if user_direction == "S":
        next_move = player.current_room.s_to
        if next_move == None:
            print("You are block, try picking different road")
        else:
            player.current_room = next_move

# East
    if user_direction == "E":
        next_move = player.current_room.e_to
        if next_move == None:
            print("You are block, try picking different road")
        else:
            player.current_room = next_move

    # West
    if user_direction == "W":
        next_move = player.current_room.w_to
        if next_move == None:
            print("You are block, try picking different road")
        else:
            player.current_room = next_move

    if user_direction == "Q":
        print(f"Thanks for playing {user_name}! Come back soon!")
        game_on = False



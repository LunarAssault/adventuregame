from adventurelib import *


@when("yell")
def yell():
    print("a hideous screech leaves your mouth")

@when("look")
def look():
    print(current_room)

@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        print(f'You go {direction}.')
        look()



dungeon = Room("""

This small room pulses with a quiet, dark light. Walls made of an inidentified black rock feel warm to the touch, and are completely smooth. 
The room itself is oddly shaped, much taller than it is wide, with one tall door to the north.

""")

hallway = Room("""
A long, narrow hallway stretches on for about 30 meters. Small scones on the wall illuminate it with flickering light.
""")
dungeon.north = hallway
current_room = dungeon

start()
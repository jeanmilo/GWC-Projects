start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant white room.
You're about to be late for the season premiere of Cole Sprouse's new reality show: Cold Sprouts and Guests.
You really want to watch that show, so you have to manage a way to escape.
There are three doors, one on your right and one on your left.
Realizing this is your only way, you decide to turn...
'''
print(start)
print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print("You turn left, but before you are able to put your hand on the door's handle, the Kool Aid man busts in through the door."
          + " The debris took a huge toll on your health and has incapitated you. how disappointing. /;" )
    
elif user_input == "right":
    print("You choose to go right and walk through the door. A wild Arceus appears! He blocks the exit, preventing you from escaping this battle."
          "You must decide quickly if you will attack or wait for it to strike first." +
          "Type 'attack' to attack, or type 'fucking coward' to not attack the pokémon")
    user_input01 = input()
    while user_input01 != "attack" and user_input01 != "fucking coward":
        print ("type 'attack' or 'fucking coward' you dipshit!!")
        user_input01 = input()
    if user_input01 == "attack":
        print("You attack the pokémon! He swiftly dodges, moving to the side away from the door. A chance to escape appears! Do you take it?"
              +" Type 'yes' to escape or type 'no' to stay behind and finish your battle.")
    elif user_input01 == 
        user_input02 = input()
        if user_input02 == "yes":
            print("You did it! You escaped! You ")
        elif user_input == "   ":
            print("Ok... Well. That didn't really accomplish anything. He's still there. Just standing there. " +
                  "But since you are so insistent on not fighting, and neither is he, you end up staying stuck in that room forever." +
                  "Congrats. You died and missed the premiere.")

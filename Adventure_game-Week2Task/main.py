import random

rooms = {
    1: {
        "name": "Room 1",
        "description": "You entered Room 1. It's dark and musty.",
        "storyline": "In this room, you find a faintly glowing orb that guides your way."
    },
    2: {
        "name": "Room 2",
        "description": "You entered Room 2. It feels cold and eerie.",
        "storyline": "A mysterious voice echoes: 'Choose wisely to continue your journey.'"
    },
    3: {
        "name": "Room 3",
        "description": "You entered Room 3. It's filled with strange symbols.",
        "storyline": "You notice a hidden message written on the wall, hinting at the right path."
    },
    4: {
        "name": "Final Room",
        "description": "You entered the Final Room. A feeling of accomplishment washes over you.",
        "storyline": "The room is filled with a warm light, revealing a treasure chest at the center."
    }
}

correct_rooms = {1: 2, 2: 3, 3: 1, 4: 2}


def display_room_info(room_num):
    print(rooms[room_num]["description"])
    print(rooms[room_num]["storyline"])


def display_intro():
    print("Welcome to the Room Adventure Game!")
    print("You have to choose the right room to survive.")
    print("There are three stages. Choose wisely.")


def get_choice(stage):
    while True:
        print(f"\nStage {stage}: Choose a room (1, 2, or 3): ")
        choice = input()
        if choice.isdigit() and 1 <= int(choice) <= 3:
            return int(choice)
        else:
            print("Invalid choice. Enter a number between 1 and 3.")


def play_game():
    display_intro()
    player_stage = 1
    while player_stage <= 4:
        print("\n" + "-"*20)
        current_room = get_choice(player_stage)
        if player_stage < 4:
            if current_room == correct_rooms[player_stage]:
                display_room_info(current_room)
                player_stage += 1
            else:
                print("Oh no! You entered the wrong room and died!")
                print("Game Over!")
                break
        else:
            if current_room == correct_rooms[player_stage]:
                display_room_info(current_room)
                print("\nCongratulations! You have reached the end of the adventure!")
                break
            else:
                print(
                    "You entered the wrong room in the final stage and the journey ends here.")
                print("Game Over!")
                break


play_game()

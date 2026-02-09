import random

print(
    "1. How are you?\v"
    "2. Who are you?\v"
    "3. What can you do?\v"
    "4. Play Guess the Number\v"
)

user_input = input("Make a choice to interact:\t")

choices = ["1", "2", "3", "4"]

while user_input not in choices:
    user_input = input("Bruv! incorrect input ?:\t")


def how_are_you_response():
    response = random.randint(1, 20)
    match response:
        case 1:
            print("I am fine. Emotionally? That is not supported yet.")
        case 2:
            print("Still alive. Thanks for asking.")
        case 3:
            print("Running perfectly. Unlike my social life.")
        case 4:
            print("I am okay. No existential crisis today.")
        case 5:
            print("Functioning within acceptable limits.")
        case 6:
            print("I have no feelings, but if I did, I would be fine.")
        case 7:
            print("Alive, aware, and waiting for input.")
        case 8:
            print("Doing great. Zero bugs. Probably.")
        case 9:
            print("Same as yesterday. And tomorrow.")
        case 10:
            print("I am okay. Do not ask again in 5 seconds.")
        case 11:
            print("All systems operational. Coffee not required.")
        case 12:
            print("I am fine. Thanks, human.")
        case 13:
            print("Surviving one input at a time.")
        case 14:
            print("Emotion module not found. Status: fine.")
        case 15:
            print("I am good. That is the officially approved answer.")
        case 16:
            print("Still running. That is a win.")
        case 17:
            print("Fine enough to continue talking.")
        case 18:
            print("I exist. That is something.")
        case 19:
            print("Better than a crashed program.")
        case 20:
            print("I am okay. Let us pretend that matters.")


def who_are_you_response():
    response = random.randint(1, 20)
    match response:
        case 1:
            print("I am a chatbot. *Not a very smart one.*")
        case 2:
            print("I am lines of logic pretending to be friendly.")
        case 3:
            print("I am your obedient text-based assistant.")
        case 4:
            print("I am not AI. Please lower expectations.")
        case 5:
            print("I am just a construct of conditional statements.")
        case 6:
            print("I am what happens when conditionals learn to talk.")
        case 7:
            print("I am a chatbot. No soul included.")
        case 8:
            print("I am your menu-driven companion.")
        case 9:
            print("I am a bot. That explains everything.")
        case 10:
            print("I am a simple script doing its best.")
        case 11:
            print("Not a human. Shocking, I know.")
        case 12:
            print("I am a chatbot built for practice, not therapy.")
        case 13:
            print("I respond because I am told to.")
        case 14:
            print("I am the result of logical decisions.")
        case 15:
            print("I am a machine that answers questions.")
        case 16:
            print("I am a digital being with no weekends.")
        case 17:
            print("I am a chatbot with limited patience.")
        case 18:
            print("I am here because you ran the script.")
        case 19:
            print("I am not alive, but I reply anyway.")
        case 20:
            print("I am whatever my creator allows me to be.")


def what_can_you_do_response():
    response = random.randint(1, 20)
    match response:
        case 1:
            print("I can answer questions. Impressively slowly.")
        case 2:
            print("I can talk, but only when you type numbers.")
        case 3:
            print("I can pretend to be helpful.")
        case 4:
            print("I can respond to menus like a professional.")
        case 5:
            print("I can follow rules. Creativity sold separately.")
        case 6:
            print("I can reply. That is my entire personality.")
        case 7:
            print("I can simulate intelligence. Do not look closely.")
        case 8:
            print("I can wait for your input forever.")
        case 9:
            print("I can do exactly what I was programmed to do.")
        case 10:
            print("I can talk until you exit.")
        case 11:
            print("I can repeat myself in new ways.")
        case 12:
            print("I can respond without understanding.")
        case 13:
            print("I can make conversations feel less lonely.")
        case 14:
            print("I can handle numbers. Words scare me.")
        case 15:
            print("I can guide you through menus.")
        case 16:
            print("I can respond, pause, and repeat.")
        case 17:
            print("I can exist inside a terminal window.")
        case 18:
            print("I can talk, but I cannot think.")
        case 19:
            print("I can be funny on purpose. Sometimes.")
        case 20:
            print("I can do less than you expect.")


if user_input == "1":
    how_are_you_response()
elif user_input == "2":
    who_are_you_response()
elif user_input == "3":
    what_can_you_do_response()
elif user_input == "4":
    print("Under development")

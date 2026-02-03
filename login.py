import datetime

user = 47, "AGENT 47", "NoWitnesses@47"  # userid, username, password


def login():
    current_time = datetime.datetime.now()
    print(
        """============================================================
            International Contract Agency Facility
============================================================"""
    )
    print("Please enter your credentials to proceed:")
    user_id = int(input("\vAgent ID:\t"))
    # todo: fix error when alphabetical id is given and it is converted into a int
    while user_id != user[0]:
        print("\v* Note: Unauthorized access is prohibited.")
        user_id = int(input("Incorrect Agent ID. Please try again:\t"))

    pass_word = input(f"Please enter password for {user_id}:\t")
    while pass_word != user[2]:
        pass_word = input("Incorrect password. Please try again:\t")

    print(
        f"\vWelcome {user[1]}, You logged in at {current_time.strftime("%H:%M:%S")}\n"
    )


login()

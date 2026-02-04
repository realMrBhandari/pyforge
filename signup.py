#! Simple signup form using set, due to it's nature of registering only unique values. Hence a good candiate for a initial onboarding check for unique username and email
usernames = {
    "tony_stark",
    "peter_parker",
    "wanda_maximoff",
    "thor_odinson",
    "tchalla_wakanda",
}

emails = {
    "tony.stark@avengers.com",
    "peter.parker@avengers.com",
    "wanda.maximoff@avengers.com",
    "thor.odinson@asgard.com",
    "tchalla@wakanda.gov",
}

print(
    """============================================================
                     Create an account
============================================================"""
    """
        Please enter your details to create an account\v
"""
)
user_email = input("Enter your email address:\t ")
while user_email.lower() in emails:
    user_email = input("Email already exists, try again:\t ")
emails.add(user_email.lower())


user_name = input("\vEnter your desired username:\t ")
while user_name.lower() in usernames:
    user_name = input("Username already taken, try again:\t ")
usernames.add(user_name.lower())

print(
    f"\vCongratulations {user_name}! Your account has been successfully created. Please check your email {user_email} for further instructions."
)

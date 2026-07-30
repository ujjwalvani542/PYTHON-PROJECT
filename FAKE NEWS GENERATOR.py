# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it
import random 

subjects=[
    "MODI JI",
    "PRIYANKA GANDHI",
    "YOGI JI ",
    "CAT ",
    "ARYAN GUPTA",
    "ARYAN SINGHA",
    "DOG"

]

actions=[
    "PLAYING IN IPL",
    "DESTROY BY RAHUL GANDHI",
    "ADRESING THE COUNTRY",
    "BATING",
    "playing playstation  ",
    "AI WOULD TAKE THE JOB",
    "CAT IS BITTEN BY "
]


places_or_things=[
    "INDORE",
    "RED FORT ",
    "DELHI",
    "PARLIAMENT",
    "PAKISTAN",
    "ENGLAND",
    "AT INDIA GATE"
]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    places=random.choice(places_or_things)


    headline= f"BREAKING NEWS:{subject} {action} {places} "
    print(headline)
    user_input=input("DO YOU WANT ANOUTHER BREAKING NEWS? PRESS (y/n):").strip()

    if user_input=='n':
        break


print("THANK YOU FOR USING FAKE NEWS GENERATOR !! HAVE AN NICEDAY")


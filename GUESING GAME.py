import random 
#PASSWORD GUSSEING SYSTEM
easy_word=["UJJWAL","MANGO","AAMPAPAD","ADMIGADHA HAI","CHUTIYE","DEAD HUMANITY"]
midium_word=["UJJWAL@2129","BHAVYE DEAD","VALORANT","GTA5"]
hard_word=["hahhahahah","auuuuu","yupbaby","heilhitler","yummy"]

print("WELCOME TO GAME")
print("ENTER THE DIFFICULTY LEVEL:easy,medium and hard")

level=input('Enter the difficulty level:').lower()

if level=="easy":
    secret=random.choice(easy_word)
elif level=="medium":
    secret=random.choice(midium_word)
elif level=="hard":
    secret=random.random(hard_word)

else:
    print("invalid option")

attempts=0
print("/n GUESS THE SECRET OUTPUT")

while True:
    guess=input("ENTER YOUR GUESS:")
    attempts+=1

    if guess==secret:
        print("CONGRATS YOUR GUESS WAS CORRECT")
        break
    hint=""
    for i in range(len(secret)):
        if i<len(guess) and guess[i]==secret[i]:
            hint+=secret[i]

        else:
            hint+="_"

    print("HINT:",hint)

print("GAME OVER")






#if choice==easy:

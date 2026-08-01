import os 
print("WELCOME TO ROBOPLAY")

while True:
    
    x=input("ENTER WHAT DO YOU WANT OT ME TO SPEAK:")
    if x=="Q":
        break
    command= f"say {x}"
    os.system(command)

    

    

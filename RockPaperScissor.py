import random
choice = ["paper", "scissor", "rock"]
tie=0
win=0
lose=0
while True:
    q = str(input("Paper,Scissor,or Rock?  ")).lower()
    c=random.choice(choice)#good info...here it get overwritten everytime the loop start over
    while (q != "paper" and q != "scissor" and q != "rock"):
        q = str(input("Paper,Scissor,or Rock?  ")).lower()
    if (q == c):
        print(c)
        print("Draw!")
        tie=tie+1
    elif (q == "scissor" and c == "rock"):
        print(c)
        print("You lost")
        lose=lose+1
    elif (q == "rock" and c == "scissor"):
        print(c)
        print("You won")
        win=win+1
    elif (q == "paper" and c == "rock"):
        print(c)
        print("You won")
        win=win+1
    elif (q == "rock" and c == "paper"):
        print(c)
        print("You lost")
        lose=lose+1
    elif (q == "scissor" and c == "paper"):
        print(c)
        print("you won")
        win=win+1
    elif (q == "paper" and c == "scissor"):
        print(c)
        print("you lost")
        lose=lose+1
    print(f"Wins : {win}\nLoses : {lose}\nTies : {tie}")
    p=int(input("Do you want to play again...enter 1 for 'Yes', otherwise  for 'No'?  "))
    if(p==1):
        continue
    else:
        print("Game ended")
        break

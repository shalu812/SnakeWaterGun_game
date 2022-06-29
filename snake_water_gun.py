import random

def game(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False

print("Computer Turn: Snake(s) water(w) or gun(g): ")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
    
you=input("Your's Turn: Snake(s) water(w) or gun(g): ")

a=game(comp,you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a== None:
    print("Game is tie")
elif a == True:
    print("You Won")
elif a == False:
    print("You Loose")


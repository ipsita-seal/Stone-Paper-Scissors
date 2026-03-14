#rock paper scissors
#rock wins over scissors
#paper wins over rock
#scissors wins over paper
import random
def fun(x,y):
    if x==y:
        print("Draw\n")
        return "draw"
    else:
        if x=='R' and y=='S':
            print('Comp:', x, 'user:',y,'\nComputer wins\n')
            return "comp"
        elif x=='P' and y=='R':
            print('Comp:', x, 'user:',y,'\nComputer wins\n')
            return "comp"
        elif x=='S' and y=='P':
            print('Comp:', x, 'user:',y,'\nComputer wins\n')
            return "comp"
        else:
            print('Comp:', x, 'user:',y,'\nUser wins\n')
            return "user"
choices=['R','P','S']
Uscore=0
Cscore=0
print("To stop, press E")
while True:
    comp=random.choice(choices)
    hand=input("enter R for rock, P for paper or S for scissors: ")
    hand=hand.upper()
    if hand == 'E':
        print("Game exited successfully")
        break
    if hand not in choices:
        print("wrong input, enter R,P or S only\n")
        continue
    result = fun(comp,hand)
    if result == "user":
        Uscore += 1
    elif result == "comp":
        Cscore += 1
print("Score -> User:", Uscore, "| Computer:", Cscore,"\n")

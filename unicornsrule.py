""" My """

import colors as derpynessrules
from utils import ask

intro = derpynessrules.red + "Welcome to deh Pink Fluffy Unicorns test! Now lets test your knoledge of Unicorns! If you dont know anything about them then go watch My Little Pony!"

def q1():
    answer = ask("What color are deh Unicorns?")
    if answer == "pink":
        print(derpynessrules.yellow + "Correct! You got it right. Now try to get the next one right!")
        return True
    print(derpynessrules.blue + "Oh no! You got it wrong! Try it again.")
    return False 

def q2():
    answer = ask("What are deh Unicorns dancing on?")
    if answer.startswith("rainbow"):
        print(derpynessrules.yellow + "Correct! You got it right. Now try to get the next one right!")
        return True
    print(derpynessrules.blue + "Oh no! You got it wrong! Try it again.")
    return False 

def q3():
    answer = ask("Use one word to descride their magical fur?")
    if answer.startswith("smiles"):
        print(derpynessrules.yellow + "Correct! You got it right. This is the end of this quiz YEAH!:)")
        return True
    print(derpynessrules.blue + "Oh no! You got it wrong! Try it again.:<")
    return False 

questions = [q1,q2,q3]

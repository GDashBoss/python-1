"""My utilities module"""

import colors as c

def ask(question):
    print(c.red + question)
    answer = input("> ")
    answer = answer.lower().strip()
    print(c.reset,end="")
    return answer

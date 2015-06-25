"""My utilities module"""

import colors as c

def ask(question):
    print(c.orange + question)
    answer = input(' ' + c.pink).lower().strip()
    return answer

if __name__ == "__main__":
    name = ask("what is your name?")
    print(name)

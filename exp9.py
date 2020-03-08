from sys import exit

def gold_room():
    next=raw_input(">")
    if "0" in next or "1" in next:
        how_much=int(next)
    else:
        dead("man,learn to type a no")
    if how_much<50:
        print"you are n't greedy"
        exit(1)
    else:
        dead("you greedy bastard")
gold_room()


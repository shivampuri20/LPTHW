things="apples oranges grapes crawnberry banana almonds"
print "wait there not complete 10 items"
stuff=things.split(' ')
more_stuff =["peanuts","food","alcohol","drinks"]
while len(stuff) !=10:
    next=more_stuff.pop()
    stuff.append(next)
    print "there is %d elements"%len(stuff)
print "here is stuff:",stuff
print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join (stuff)
print '#'.join(stuff[3:6])

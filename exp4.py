from sys import argv
script , file1=argv
def printall(f):
    print f.read()
def rewind(f):
    f.seek(0)
def  current_file(currentline ,f):
    print currentline ,f.readline()
currentfile = open(file1,'r')
printall (currentfile)
rewind  (currentfile)
currline=1
current_file(currline, currentfile)
currline=currline+1
current_file(currline ,currentfile)

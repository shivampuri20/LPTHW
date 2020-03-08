from sys import argv
from os.path import exists 
script ,file1 ,file2 =argv
target=open(file1,'r')
input=target.read()
print "file is %d long "% len(input)
print"checking file exists: %s" % exists(file2)
target1= open(file2,'w')
target1.write(input)
target.close()
target1.close()

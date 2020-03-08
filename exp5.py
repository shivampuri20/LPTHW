print "let do \" everything "
print 'you \'d need to know escapes with \\ that do \n newline and \t tabs/'
poem ="""
we are 
peoples that can
make people life 
affordable 
and interesting 
"""
print poem 
five =10-2+3-6
print "five: ",five 
print "five: %d"% five 

def secret_formula(started):
    jelly=started*500
    jars=jelly/1000
    crates=jars/100
    return jelly ,jars ,crates

start=10000
jelly,jars,crates=secret_formula(start)
print"we have %d jellies %d jars and %d crates"%(jelly,jars,crates)
start=start/10
print"we have %d jellie %d jars and %d crates "%secret_formula(start)

element=[]
def function(i,x,n):
    if i<x :
        print "number is %d"%i
        element.append(i)
        i=i+n
        
        function(i,x,n)
    print "element",element
function(0,6,2)
for num in element:
    print " no in %d"% num

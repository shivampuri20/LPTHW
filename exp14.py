class thing(object):
    def __init__(self):
        self.number =0
    
    def function(self):
        print("i got called")

    def add_me(self,more):
        self.number+=more
        return self.number

a=thing()
b=thing()
a.function()
b.function()

print a.add_me(20)
print b.add_me(30)
print a.add_me(40)
print a.number
print b.number

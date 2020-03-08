cities={'himachal':'Shimla' ,'punjab':'chandigarh','rajasthan':'jaipur'}
cities['ny']='new york'
cities['or']='portland'
def find_city(themap ,state):
    if state in themap:
        del themap[state]
    else:
        return "not found"

cities['find']=find_city  #changing function in dicts same as above 
while True:
    print "state!"
    state=raw_input('>')
    if not state: 
        break
    city_found=cities['find'](cities,state) #dict mapping 
    print city_found


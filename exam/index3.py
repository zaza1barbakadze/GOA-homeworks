def ხალხის_რაოდენობა(bus_stops):
    people_on_bas = 0
    for on, off in bus_stops :
        people_on_bas += on
        people_on_bas -= off
    return people_on_bas     

print(ხალხის_რაოდენობა([(10,0), (3,5), (5,8)]))
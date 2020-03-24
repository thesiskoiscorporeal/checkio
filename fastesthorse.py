def fastest_horse(horses: list) -> int:
    
    nRaces = len(horses)
        
    dictRaces = { i : 0 for i in range(nRaces)} #construct dict with keys indexes from 0 to nRaces-1 and values 0
    
    i = 0 #counter for race index to 0
    for race in horses: #iterate over races
        dictRaces[i] = race.index(min(race))
        i += 1 #increment counter

    #find most commonly occuring value in dictRaces
    track={}
    for key,value in dictRaces.items():
        if value not in track:
            track[value]=0
        else:
            track[value]+=1
            
    return (max(track,key=track.get) + 1) #offset index by +1


print(fastest_horse([["1:10","1:15","1:20"],["1:05","1:10","1:15"],["2:59","2:59","2:59"]]))
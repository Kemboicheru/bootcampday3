def find_max_min(inputarray):
    sortedarray = sorted(inputarray)
    returnarray = []
    
    returnarray.append(sortedarray[0])
    returnarray.append(sortedarray[len(inputarray)-1])
    
    return returnarray
    

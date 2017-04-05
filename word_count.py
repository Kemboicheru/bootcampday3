def words(wordstring):
    
    #make an array of words from the string
    wordarray = str(wordstring).split(" ")
    returnarray = {}
    
    #loop through and assign lenght to items
    for item in wordarray:
        if len(item) > 0:
            if item in returnarray:
                returnarray[item] += 1
            else:
                returnarray[item] = 1

    return returnarray


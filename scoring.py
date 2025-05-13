import math
def scoring(nameTimeDict, wrTime, maxScore, minActivity):
    numRuns = len(nameTimeDict)
    modifier = min(math.sqrt(numRuns/minActivity), 1) #punishes low population boards, but grows quickly ealry
    nameScoreDict = {}
    for key in nameTimeDict:
        nameScoreDict[key] = maxScore*pow(wrTime/nameTimeDict[key],2) * modifier #calc score 
    return(nameScoreDict)

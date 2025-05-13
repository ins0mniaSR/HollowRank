def mainBoardScoring(nameTimeDict, wrTime):
    nameScoreDict = {}
    for key in nameTimeDict:
        nameScoreDict[key] = 100000*pow(wrTime/nameTimeDict[key],2)
    return(nameScoreDict)
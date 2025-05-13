from srcImporter import srcImport
from mainBoardScoring import mainBoardScoring
from srcVars import catIdDict, gameId, numCats
from csvExporter import csvExport

nameTimeDict = {}
wrTimeDict = {}
for category in catIdDict: #fetching run information from src
    nameTimeDict[category], wrTimeDict[category] = srcImport(gameId, catIdDict[category][0], catIdDict[category][1], catIdDict[category][2])

nameScoreDict = {} #score runs and return name and scores per cat
for category in nameTimeDict:
    nameScoreDict[category] = mainBoardScoring(nameTimeDict[category], wrTimeDict[category])

playerCatScoresDict = {} #create dict with name: list of scores
for category in nameScoreDict:
    for name in nameScoreDict[category]:
        playerCatScoresDict.setdefault(name, []).append(nameScoreDict[category][name])


sortedPlayerScoresDict = {} #sort list to apply diminishing value in order of run score
for name in playerCatScoresDict:
    sortedPlayerScoresDict[name] = sorted(playerCatScoresDict[name],reverse=True)

playerScoreTotalDict = {} #apply modifiers and return dict of name : score
for name in sortedPlayerScoresDict:
    playerScoreTotalDict[name] = 0
    for pos in range(0, len(sortedPlayerScoresDict[name])):
        playerScoreTotalDict[name] += sortedPlayerScoresDict[name][pos]*pow(0.5,pos)

sortedScoreDict = dict(sorted(playerScoreTotalDict.items(), key=lambda item: item[1], reverse=True)) #sort the above

csvExport(sortedScoreDict) #export to csv to paste into google sheets





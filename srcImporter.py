from speedruncompy.endpoints import *
from speedruncompy import GetGameLeaderboard2

def srcImport(gameIdIn, categoryDefinition):
    categoryId = categoryDefinition[0]
    values = []
    for varValue in categoryDefinition[1]: # for each of the (variableId, valueId) tuples
        values.append(VarValues({"variableId": varValue[0], "valueIds": [varValue[1]]}))

    result = GetGameLeaderboard2(gameIdIn, categoryId=categoryId, values=values).perform()
    playerDict = {p.id: p for p in result.playerList}
    if len(result.runList) == 0:
        return ({},0)
    wr = result.runList[0].time
    nameTimeDict = {}
    for run in result.runList:
        nameTimeDict[playerDict[run.playerIds[0]].name] = run.time
    return(nameTimeDict, wr)

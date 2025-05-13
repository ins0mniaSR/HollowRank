from speedruncompy.endpoints import *
from speedruncompy import GetGameLeaderboard2

def srcImport(gameIdIn, categoryIdIn, variableIdIn, valueIdsIn):
    result = GetGameLeaderboard2(gameId=gameIdIn, categoryId=categoryIdIn, values=[{"variableId": variableIdIn, "valueIds": [valueIdsIn,]}]).perform_all()
    playerDict = {p.id: p for p in result.playerList}
    wr = result.runList[0].time
    nameTimeDict = {}
    for run in result.runList:
        nameTimeDict[playerDict[run.playerIds[0]].name] = run.time
    return(nameTimeDict, wr)

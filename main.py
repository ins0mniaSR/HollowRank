### TODO Add ILs, Console Runs, Modded. Tweak scoring, possibly raise min activity thresholds for mainboard to 50?

from srcVars import nmgMainCatIdDict, glitchedMainCatIdDict, nmgExtensionCatIdDict, glitchedExtensionCatIdDict, mainGameId, extensionGameId 
from csvExporter import csvExport
import config
from boardScoringHandler import boardHandler

sortedScoreDict = {}
finishedFetching = 0
outputCsv = 0
boardsFetched = {"nmgMain" : False, "glitchedMain" : False, "nmgExtensions" : False, "glitchedExtensions" : False, "nmgTotal" : False, "glitchedTotal" : False}
while finishedFetching == 0:
    userIn = input("Select which boards you want to fetch data for: \n 1: NMG Mainboard \n 2: Glitched Main \n 3: NMG Extensions \n 4: Glitched Extensions \n")
    if userIn == "1": # NMG Main Boards
        print("Fetching NMG Main Boards...")
        sortedScoreDict["nmgMain"] = boardHandler(mainGameId, nmgMainCatIdDict, config.mainScoreMax, config.nmgMainActiveNum, config.mainDecayMod)
        boardsFetched["nmgMain"] = True
        print("Fetched NMG Main Boards!\n")
    elif userIn == "2": # Glitched Main Boards
        print("Fetching Glitched Main Boards...")
        sortedScoreDict["glitchedMain"] = boardHandler(mainGameId, glitchedMainCatIdDict, config.mainScoreMax, config.glitchedMainActiveNum, config.mainDecayMod)
        boardsFetched["glitchedMain"] = True
        print("Fetched Glitched Main Boards!\n")
    elif userIn == "3": # NMG Extension Boards
        print("Fetching NMG Extension Boards...")
        sortedScoreDict["nmgExtension"] = boardHandler(extensionGameId, nmgExtensionCatIdDict, config.extensionScoreMax, config.nmgExtensionActiveNum, config.extensionDecayMod)
        boardsFetched["nmgExtensions"] = True
        print("Fetched NMG Extension Boards!\n")
    elif userIn == "4":
        print("Fetching Glitched Extension Boards...") # Glitched Extension Boards
        sortedScoreDict["glitchedExtension"] = boardHandler(extensionGameId, glitchedExtensionCatIdDict, config.extensionScoreMax, config.glitchedExtensionActiveNum, config.extensionDecayMod)
        boardsFetched["glitchedExtensions"] = True
        print("Fetched Glitched Extension Boards!\n")
    else:
        print("Invalid input\n")
    userIn = input("Are you finished fetching boards? (Y to proceed)\n")
    if userIn == "Y":
        finishedFetching = 1

# Make summed total scores for NMG / Glitched / Overall
print("Calculating applicable combined scores...")
if boardsFetched["nmgMain"] == True and boardsFetched["nmgExtensions"] == True: # Combined NMG board if both were fetched
    boardsFetched["nmgTotal"] = True
    nmgCats = ["nmgMain", "nmgExtension"]
    totalNmgScoreDict = {}
    for category in nmgCats:
        for name in sortedScoreDict[category]:
            totalNmgScoreDict[name] = totalNmgScoreDict.setdefault(name, 0) + sortedScoreDict[category][name]
    sortedScoreDict["nmgTotal"] = dict(sorted(totalNmgScoreDict.items(), key=lambda item: item[1], reverse=True))
if boardsFetched["glitchedMain"] == True and boardsFetched["glitchedExtensions"] == True: # Combined Glitched board if both were fetched
    boardsFetched["glitchedTotal"] = True
    glitchedCats = ["glitchedMain", "glitchedExtension"]
    totalGlitchedScoreDict = {}
    for category in glitchedCats:
        for name in sortedScoreDict[category]:
            totalGlitchedScoreDict[name] = totalGlitchedScoreDict.setdefault(name, 0) + sortedScoreDict[category][name]
    sortedScoreDict["glitchedTotal"] = dict(sorted(totalGlitchedScoreDict.items(), key=lambda item: item[1], reverse=True))
if boardsFetched["nmgTotal"] == True and boardsFetched["glitchedTotal"] == True: #Total board if all were fetched
    totalScoreDict = {}
    for category in sortedScoreDict:
        for name in sortedScoreDict[category]:
            totalScoreDict[name] = totalScoreDict.setdefault(name, 0) + sortedScoreDict[category][name]
    sortedScoreDict["total"] = dict(sorted(totalScoreDict.items(), key=lambda item: item[1], reverse=True)) 

print("Created applicable combined scores!\nCreating .csv...")

#Export score totals for data that has been generated, to their respective .csv file
for exportBoard in sortedScoreDict:
    csvExport(sortedScoreDict[exportBoard], config.exportFilenames[exportBoard])
print("\nComplete!")
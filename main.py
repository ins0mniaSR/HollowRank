### TODO Add ILs, Console Runs, Modded. Tweak scoring, possibly raise min activity thresholds for mainboard to 50?

from srcVars import nmgMainCatIdDict, glitchedMainCatIdDict, nmgExtensionCatIdDict, glitchedExtensionCatIdDict, mainGameId, extensionGameId 
from csvExporter import csvExport
import config
from boardScoringHandler import boardHandler

sortedScoreDict = {}
catPlayerScoreDict = {}
finishedFetching = False
boardsFetched = {"nmgMain" : False, "glitchedMain" : False, "nmgExtension" : False, "glitchedExtension" : False, "nmgTotal" : False, "glitchedTotal" : False}
while finishedFetching == False:
    userIn = input("Select which boards you want to fetch data for: \n 1: NMG Mainboard \n 2: Glitched Main \n 3: NMG Extension \n 4: Glitched Extension \n") # Handle the response to this as one thing using dicts instead of 4 elifs and add a fetch all
    if userIn == "1": # NMG Main Boards
        print("Fetching NMG Main Boards...")
        sortedScoreDict["nmgMain"], catPlayerScoreDict['nmgMain'] = boardHandler(mainGameId, nmgMainCatIdDict, config.mainScoreMax, config.nmgMainActiveNum, config.mainDecayMod)
        boardsFetched["nmgMain"] = True
        print("Fetched NMG Main Boards!\n")
    elif userIn == "2": # Glitched Main Boards
        print("Fetching Glitched Main Boards...")
        sortedScoreDict["glitchedMain"], catPlayerScoreDict["glitchedMain"] = boardHandler(mainGameId, glitchedMainCatIdDict, config.mainScoreMax, config.glitchedMainActiveNum, config.mainDecayMod)
        boardsFetched["glitchedMain"] = True
        print("Fetched Glitched Main Boards!\n")
    elif userIn == "3": # NMG Extension Boards
        print("Fetching NMG Extension Boards...")
        sortedScoreDict["nmgExtension"], catPlayerScoreDict["nmgExtension"] = boardHandler(extensionGameId, nmgExtensionCatIdDict, config.extensionScoreMax, config.nmgExtensionActiveNum, config.extensionDecayMod)
        boardsFetched["nmgExtension"] = True
        print("Fetched NMG Extension Boards!\n")
    elif userIn == "4":
        print("Fetching Glitched Extension Boards...") # Glitched Extension Boards
        sortedScoreDict["glitchedExtension"], catPlayerScoreDict["glitchedExtension"] = boardHandler(extensionGameId, glitchedExtensionCatIdDict, config.extensionScoreMax, config.glitchedExtensionActiveNum, config.extensionDecayMod)
        boardsFetched["glitchedExtension"] = True
        print("Fetched Glitched Extension Boards!\n")
    else:
        print("Invalid input\n")
    validResponse = False
    while validResponse == False:
        userIn = input("Are you finished fetching boards? Y/N: ")
        if userIn == "Y":
            finishedFetching = True
            validResponse = True
        elif userIn == "N":
            validResponse = True
        else:
            print("Invalid Response!")

# Make summed total scores for NMG / Glitched / Overall
print("Calculating applicable combined scores...")
if boardsFetched["nmgMain"] == True and boardsFetched["nmgExtension"] == True: # Combined NMG board if both were fetched
    boardsFetched["nmgTotal"] = True
    nmgCats = ["nmgMain", "nmgExtension"]
    totalNmgScoreDict = {}
    for category in nmgCats:
        for name in sortedScoreDict[category]:
            totalNmgScoreDict[name] = totalNmgScoreDict.setdefault(name, 0) + sortedScoreDict[category][name]
    sortedScoreDict["nmgTotal"] = dict(sorted(totalNmgScoreDict.items(), key=lambda item: item[1], reverse=True))
if boardsFetched["glitchedMain"] == True and boardsFetched["glitchedExtension"] == True: # Combined Glitched board if both were fetched
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

finishedIndividuals = False
while  finishedIndividuals == False:
    validResponse = False
    while validResponse == False:
        userIn = input("\nDo you want the results for a specific user? Y/N: ")
        if userIn == "Y" or userIn == "N":
            validResponse = True
        else:
            print("Invalid input!")

    if userIn == "Y":
        player = input("\nType the player's username as it appears on SRC: ")
        individualScoresDict = {}
        for boardType in boardsFetched:
            if boardsFetched[boardType] == True and "Total" not in boardType:
                for individualCategory in catPlayerScoreDict[boardType]:
                    if catPlayerScoreDict[boardType].setdefault(individualCategory, player).setdefault(player, 0) != 0:
                        individualScoresDict[individualCategory] = catPlayerScoreDict[boardType].setdefault(individualCategory, player).setdefault(player, 0)
        print("Exporting to ", player, "Scores.csv", sep='')
        csvExport(individualScoresDict, (player + "Scores.csv"))
    if userIn == "N":
        finishedIndividuals = True

print("Created applicable combined scores!\nCreating .csv...")

#Export score totals for data that has been generated, to their respective .csv file
for exportBoard in sortedScoreDict:
    csvExport(sortedScoreDict[exportBoard], config.exportFilenames[exportBoard])
print("\nComplete!")
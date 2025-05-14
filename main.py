from srcVars import nmgMainCatIdDict, glitchedMainCatIdDict, nmgExtensionCatIdDict, glitchedExtensionCatIdDict, mainGameId, extensionGameId #add glitched main board calcs @ins0mniaSR
from csvExporter import csvExport
import config
from boardScoringHandler import boardHandler

sortedScoreDict = {}

# Generate score totals
sortedScoreDict["nmgMain"] = boardHandler(mainGameId, nmgMainCatIdDict, config.mainScoreMax, config.nmgMainActiveNum, config.mainDecayMod) # NMG Main Boards
sortedScoreDict["glitchedMain"] = boardHandler(mainGameId, glitchedMainCatIdDict, config.mainScoreMax, config.glitchedMainActiveNum, config.mainDecayMod) # Glitched Main Boards
sortedScoreDict["nmgExtension"] = boardHandler(extensionGameId, nmgExtensionCatIdDict, config.extensionScoreMax, config.nmgExtensionActiveNum, config.extensionDecayMod) # NMG Extension Boards
sortedScoreDict["glitchedExtension"] = boardHandler(extensionGameId, glitchedExtensionCatIdDict, config.extensionScoreMax, config.glitchedExtensionActiveNum, config.extensionDecayMod) # Glitched Main Boards

# Make a summed total score
totalScoreDict = {}
for category in sortedScoreDict:
    for name in sortedScoreDict[category]:
        totalScoreDict[name] = totalScoreDict.setdefault(name, 0) + sortedScoreDict[category][name]

# Now sort it 
sortedTotalDict = dict(sorted(totalScoreDict.items(), key=lambda item: item[1], reverse=True)) #sort the above


#Export score totals
csvExport(sortedScoreDict["nmgMain"], config.nmgMainOutput) # Export NMG Main
csvExport(sortedScoreDict["glitchedMain"], config.glitchedMainOutput) # Export Glitched Main
csvExport(sortedScoreDict["nmgExtension"], config.nmgExtensionsOutput) # Export NMG Extensions
csvExport(sortedScoreDict["glitchedExtension"], config.glitchedExtensionsOutput) # Export Glitched Extensions
csvExport(sortedTotalDict, config.totalOutput) # Export Sums
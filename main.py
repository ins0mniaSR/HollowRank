from srcVars import nmgMainCatIdDict, glitchedMainCatIdDict, mainGameId #add glitched main board calcs @ins0mniaSR
from csvExporter import csvExport
import config
from boardScoringHandler import boardHandler

sortedScoreDict = {}

### NMG Main Boards
sortedScoreDict["nmgMain"] = boardHandler(mainGameId, nmgMainCatIdDict, config.mainScoreMax, config.nmgMainActiveNum, config.mainDecayMod) # NMG Main Boards
sortedScoreDict["glitchedMain"] = boardHandler(mainGameId, glitchedMainCatIdDict, config.mainScoreMax, config.glitchedMainActiveNum, config.mainDecayMod) # Glitched Main Boards

csvExport(sortedScoreDict["nmgMain"], config.nmgMainOutput) # Export NMG Main
csvExport(sortedScoreDict["glitchedMain"], config.glitchedMainOutput) # Export Glitched Main

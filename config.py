### Main Boards
mainScoreMax = 100000 # Default 100000
mainDecayMod = 0.5    # How quickly added runs' value decreases, defualt 0.5

nmgMainActiveNum = 100 # How many runs are needed to remove all penalties for a low run count on an NMG main board, default 20
glitchedMainActiveNum = 20 # how many runs are needed to remove all penalties for a low run count on a glitched main board, default 10

### Extension Boards
extensionScoreMax = 50000 # Default 50000
extensionDecayMod = 0.5    # How quickly added runs' value decreases, defualt 0.5

nmgExtensionActiveNum = 50 # How many runs are needed to remove all penalties for a low run count on an NMG main board, default 20
glitchedExtensionActiveNum = 10 # how many runs are needed to remove all penalties for a low run count on a glitched main board, default 10


### Export Filenames
exportFilenames = {
"nmgMain" : "nmgMainOutput.csv",
"glitchedMain" : "glitchedMainOutput.csv",
"nmgExtension" : "nmgExtensionsOutput.csv",
"glitchedExtension" : "glitchedExtensionsOutput.csv",
"nmgTotal" : "totalNmgOutput.csv",
"glitchedTotal" : "totalGlitchedOutput.csv",
"total" : "totalOutput.csv"
}

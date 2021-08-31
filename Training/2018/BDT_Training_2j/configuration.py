# example of configuration file

import os

configDir = os.path.expandvars("/afs/cern.ch/user/s/ssaumya/Projects/WW_Analysis_Work/WW_Cuts_Optimization/CMSSW_11_1_3/src/PlotsConfigurations/Configurations/WW/FullRunII/Full2018_v7/BDT_Training_2j/") #change the path to where following files are

tagName = ''

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# file with list of cuts
cutsFile = os.path.join(configDir,'cuts_BDT.py' )

# file with list of samples
samplesFile = os.path.join(configDir,'samples_BDT.py' )

# structure file for datacard
structureFile = os.path.join(configDir,'structure.py')

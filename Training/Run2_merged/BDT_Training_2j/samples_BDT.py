import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # inclusive BDT Training 2j merged 
configurations = os.path.dirname(configurations) # FullRunII
configurations = os.path.dirname(configurations) # WW
configurations = os.path.dirname(configurations) # Configurations


from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseWnAOD, addSampleWeight
def nanoGetSampleFiles_2016(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')
	
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight
def nanoGetSampleFiles_2017(inputDir, sample):
    try:
        if _samples_noload:
            return [sample]
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

def nanoGetSampleFiles_2018(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')


# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()


################################################
################# SKIMS ########################
################################################

mcProduction_2016 = 'Summer16_102X_nAODv7_Full2016v7'
mcSteps_2016 = 'MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7{var}'

mcProduction_2017 = 'Fall2017_102X_nAODv7_Full2017v7'
mcSteps_2017 = 'MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7{var}'

mcProduction_2018 = 'Autumn18_102X_nAODv7_Full2018v7'
mcSteps_2018 = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory_2016(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction_2016, mcSteps_2016.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction_2016, mcSteps_2016.format(var=''))
		
def makeMCDirectory_2017(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction_2017, mcSteps_2017.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction_2017, mcSteps_2017.format(var=''))
		
def makeMCDirectory_2018(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction_2018, mcSteps_2018.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction_2018, mcSteps_2018.format(var=''))

mcDirectory_2016 = makeMCDirectory_2016()
mcDirectory_2017 = makeMCDirectory_2017()
mcDirectory_2018 = makeMCDirectory_2018()

#########################################
############ MC COMMON ##################
#########################################

mcCommonWeight_2016 = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'
mcCommonWeight_2017 = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'
mcCommonWeight_2018 = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

###### Top #######

#xxxxxxx 2016 xxxxxxx
files = nanoGetSampleFiles_2016(mcDirectory_2016, 'TTJets_DiLept') + \
    nanoGetSampleFiles_2016(mcDirectory_2016, 'TTJets_DiLept_ext1') + \
    nanoGetSampleFiles_2016(mcDirectory_2016, 'ST_s-channel') + \
    nanoGetSampleFiles_2016(mcDirectory_2016, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles_2016(mcDirectory_2016, 'ST_t-channel_top') + \
    nanoGetSampleFiles_2016(mcDirectory_2016, 'ST_tW_antitop') + \
    nanoGetSampleFiles_2016(mcDirectory_2016, 'ST_tW_top')

samples['top_2016'] = {
    'name': files,
    'weight': mcCommonWeight_2016,
    'FilesPerJob': 4,
}

addSampleWeight(samples,'top_2016','TTJets_DiLept','Top_pTrw')

#xxxxxxx 2017 xxxxxxx
Top_pTrw_2017 = '((topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) + (topGenPt * antitopGenPt <= 0.))'

files = nanoGetSampleFiles_2017(mcDirectory_2017, 'TTTo2L2Nu') + \
    nanoGetSampleFiles_2017(mcDirectory_2017, 'ST_s-channel') + \
    nanoGetSampleFiles_2017(mcDirectory_2017, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles_2017(mcDirectory_2017, 'ST_t-channel_top') + \
    nanoGetSampleFiles_2017(mcDirectory_2017, 'ST_tW_antitop') + \
    nanoGetSampleFiles_2017(mcDirectory_2017, 'ST_tW_top')

samples['top_2017'] = {
    'name': files,
    'weight': mcCommonWeight_2017,
    'FilesPerJob': 1,
}

addSampleWeight(samples,'top_2017','TTTo2L2Nu','Top_pTrw_2017')


#xxxxxxx 2018 xxxxxxx
files = nanoGetSampleFiles_2018(mcDirectory_2018, 'TT_DiLept') + \
    nanoGetSampleFiles_2018(mcDirectory_2018, 'ST_s-channel_ext1') + \
    nanoGetSampleFiles_2018(mcDirectory_2018, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles_2018(mcDirectory_2018, 'ST_t-channel_top') + \
    nanoGetSampleFiles_2018(mcDirectory_2018, 'ST_tW_antitop_ext1') + \
    nanoGetSampleFiles_2018(mcDirectory_2018, 'ST_tW_top_ext1')

samples['top_2018'] = {
    'name': files,
    'weight': mcCommonWeight_2018,
    'FilesPerJob': 2,
}

addSampleWeight(samples,'top_2018','TT_DiLept','Top_pTrw')

###########################################
#############   SIGNALS  ##################
###########################################

###### WW ########

#xxxxxxx 2016 xxxxxxx
samples['WW_2016'] = {
    'name': nanoGetSampleFiles_2016(mcDirectory_2016, 'WW-LO'),
    'weight': mcCommonWeight_2016+ '*nllW',
    'FilesPerJob': 4
}

#xxxxxxx 2017 xxxxxxx
samples['WW_2017'] = {
    'name': nanoGetSampleFiles_2017(mcDirectory_2017, 'WW-LO'),
    'weight': mcCommonWeight_2017 + '*nllW',
    'FilesPerJob': 1
}

#xxxxxxx 2018 xxxxxxx
samples['WW_2018'] = {
    'name': nanoGetSampleFiles_2018(mcDirectory_2018, 'WW-LO'),
    'weight': mcCommonWeight_2018+'*nllW',
    'FilesPerJob': 2
}

###### ggWW ########

#xxxxxxx 2016 xxxxxxx
samples['ggWW_2016'] = {
    'name': nanoGetSampleFiles_2016(mcDirectory_2016, 'GluGluWWTo2L2Nu_MCFM'),
    'weight': mcCommonWeight_2016+'*1.53/1.4', # updating k-factor
    'FilesPerJob': 4
}

#xxxxxxx 2017 xxxxxxx
files = nanoGetSampleFiles_2017(mcDirectory_2017, 'GluGluToWWToENEN') + \
    nanoGetSampleFiles_2017(mcDirectory_2017, 'GluGluToWWToENMN') + \
    nanoGetSampleFiles_2017(mcDirectory_2017, 'GluGluToWWToENTN') + \
    nanoGetSampleFiles_2017(mcDirectory_2017, 'GluGluToWWToMNEN') + \
    nanoGetSampleFiles_2017(mcDirectory_2017, 'GluGluToWWToMNMN') + \
    nanoGetSampleFiles_2017(mcDirectory_2017, 'GluGluToWWToMNTN') + \
    nanoGetSampleFiles_2017(mcDirectory_2017, 'GluGluToWWToTNEN') + \
    nanoGetSampleFiles_2017(mcDirectory_2017, 'GluGluToWWToTNMN') + \
    nanoGetSampleFiles_2017(mcDirectory_2017, 'GluGluToWWToTNTN')

samples['ggWW_2017'] = {
    'name': files,
    'weight': mcCommonWeight_2017 + '*1.53/1.4', # updating k-factor
    'FilesPerJob': 10
}

#xxxxxxx 2018 xxxxxxx
samples['ggWW_2018'] = {
    'name': nanoGetSampleFiles_2018(mcDirectory_2018, 'GluGluToWWToENEN') + \
            nanoGetSampleFiles_2018(mcDirectory_2018, 'GluGluToWWToENMN') + \
            nanoGetSampleFiles_2018(mcDirectory_2018, 'GluGluToWWToENTN') + \
            nanoGetSampleFiles_2018(mcDirectory_2018, 'GluGluToWWToMNEN') + \
            nanoGetSampleFiles_2018(mcDirectory_2018, 'GluGluToWWToMNMN') + \
            nanoGetSampleFiles_2018(mcDirectory_2018, 'GluGluToWWToMNTN') + \
            nanoGetSampleFiles_2018(mcDirectory_2018, 'GluGluToWWToTNEN') + \
            nanoGetSampleFiles_2018(mcDirectory_2018, 'GluGluToWWToTNMN') + \
            nanoGetSampleFiles_2018(mcDirectory_2018, 'GluGluToWWToTNTN'),
    'weight': mcCommonWeight_2018+'*1.53/1.4',
    'FilesPerJob': 2
}


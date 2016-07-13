from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'TnPmcTrees25nsDR80X'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'tp_from_aod_MC.py'

config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1/AODSIM'

config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
#config.Data.totalUnits = 500
config.Data.unitsPerJob = 6
config.Data.outLFNDirBase = '/store/group/phys_muon/hbrun/muonPOGtnpTrees/MCDR80X'
config.Data.publication = False
config.Data.outputDatasetTag = 'TnPmcTrees25nsDR80X'

config.Site.storageSite = 'T2_CH_CERN'

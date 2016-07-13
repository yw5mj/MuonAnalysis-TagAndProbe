from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'TnPmcTrees25nsDR80X_TSGsampleWithTrigger'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'tp_from_aod_MC_L1stage2.py'

config.Data.inputDataset = '/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/RunIISpring16DR80-FlatPU8to37HcalNZSRAW_withHLT_80X_mcRun2_asymptotic_v14_ext1-v1/AODSIM'

config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
#config.Data.totalUnits = 500
config.Data.unitsPerJob = 4
config.Data.outLFNDirBase = '/store/group/phys_muon/hbrun/muonPOGtnpTrees/MCDR80X'
config.Data.publication = False
config.Data.outputDatasetTag = 'TnPmcTrees25nsDR80X_TSGsampleWithTrigger'

config.Site.storageSite = 'T2_CH_CERN'

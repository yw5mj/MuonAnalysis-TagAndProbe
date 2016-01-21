from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'TnPTreeMC25nsDoubleMuon76X'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'tp_from_aod_MC.py'

config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'

config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
#config.Data.totalUnits = 500
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/group/phys_muon/hbrun/muonPOGtnpTrees/doubleMuons'
config.Data.publication = False
config.Data.publishDataName = 'TnPtreesMCmadgraphNLOdoubleMuon76'

config.Site.storageSite = 'T2_CH_CERN'

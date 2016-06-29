from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'pogDoubleMuonv1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'tp_from_aod_Data_doubleMu.py'

config.Data.inputDataset = '/DoubleMuon/Run2016B-PromptReco-v2/AOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 30
config.Data.lumiMask = 'Cert_271036-274240_13TeV_PromptReco_Collisions16_JSON.txt'
config.Data.runRange = '258159'
config.Data.outLFNDirBase = '/store/group/phys_muon/hbrun/muonPOGtnpTrees/doubleMuon2016/dataPromptReco'
config.Data.publication = False
config.Data.outputDatasetTag = 'pogDoubleMuonv1'

config.Site.storageSite = 'T2_CH_CERN' 

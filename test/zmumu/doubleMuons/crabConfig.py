from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'pogDoubleMuonTreeProductionReRECO'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'tp_from_aod_Data.py'

config.Data.inputDataset = '/DoubleMuon/Run2015D-16Dec2015-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 100
config.Data.lumiMask = 'Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt'
#config.Data.runRange = '258159'
config.Data.outLFNDirBase = '/store/group/phys_muon/hbrun/muonPOGtnpTrees/DoubleMuon'
config.Data.publication = False
config.Data.outputDatasetTag = 'tpTreeDataDoubleMureRECO"'

config.Site.storageSite = 'T2_CH_CERN' 

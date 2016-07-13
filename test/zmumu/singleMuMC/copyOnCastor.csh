#!/bin/csh
echo $ROOTSYS
set list=`ls /tmp/hbrun | grep TnPtreeMC`
set compteur=0
cmsenv
cd /tmp/hbrun
foreach i ($list)
	echo $i
	@ compteur += 1
	/cvmfs/cms.cern.ch/slc6_amd64_gcc530/lcg/root/6.06.00-ikhhed4/bin/hadd dataMerged.root  /tmp/hbrun/$i/tnpZ_MC_*.root 
	cmsStage dataMerged.root /store/group/phys_muon/TagAndProbe/Run2016/80X_v3/DY_madgraphMLM/TnPTree_80X_DYLL_M50_MadGraphMLM_part$compteur.root 
        rm dataMerged.root
end

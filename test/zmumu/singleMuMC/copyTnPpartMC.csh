#!/bin/csh

setenv theEOSdir /store/group/phys_muon/hbrun/muonPOGtnpTrees/MCDR80X/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/TnPmcTrees25nsDR80X 

setenv theSubDir `eos ls $theEOSdir` 
setenv outputDir TnPtreeMC

setenv theEOSdirFull $theEOSdir/$theSubDir/0000
set list=`cmsLs $theEOSdir/$theSubDir/0000 | grep root | awk '{ print $1 }'`

set myFileCounter=0
set myIncreCounter=1 
mkdir /tmp/hbrun/$outputDir$myIncreCounter

foreach i ($list)
	echo $i
        @ myFileCounter += 1
	cmsStage $theEOSdirFull/$i /tmp/hbrun/$outputDir$myIncreCounter
	if ($myFileCounter > 100) then 
		@ myIncreCounter += 1
		set myFileCounter=0
		echo "will create the directory $myIncreCounter"
		mkdir /tmp/hbrun/$outputDir$myIncreCounter
	endif 
end

import os
import sys
import re


def createFile(int, firstRun, lastRun):
    file = open("crabConfigRunBv2.py","r")
    lines = file.readlines()
    file.close()

    outFile = open("crabConfigRunB_part"+str(int)+".py","w")
    for aLine in lines:
        print aLine
        if (len(re.split("requestName",aLine))>1):
            outFile.write("config.General.requestName = 'pogDoubleMuonv1_part"+str(int)+"'\n")
            continue
        if (len(re.split("outputDatasetTag",aLine))>1):
            outFile.write("config.Data.outputDatasetTag = 'pogDoubleMuonv1_part"+str(int)+"'\n")
            continue
        if (len(re.split("runRange",aLine))>1):
            outFile.write("config.Data.runRange = '"+str(firstRun)[1:]+"-"+str(lastRun)[1:]+"'\n")
            continue
        outFile.write(aLine)
    outFile.close()

file = open("allJson.txt","r")
runs = file.readlines()
file.close()

fullLumi = 0
listRuns = []
for line in runs:
    theRun = re.split(":",re.split("\|",line)[1])[0]
    theLumi = re.split("\|",line)[6]
    runLumi=[theRun, theLumi]
    fullLumi = fullLumi + float(theLumi)
    listRuns.append(runLumi)
print "fullLumi=",fullLumi
lumiThreshold = fullLumi/3
print "lumiThreshold=", lumiThreshold
totLumi=0
ite=0
for aRun in listRuns:
    if (totLumi==0):
        firstRun=aRun[0]
    totLumi = totLumi + float(aRun[1])
    if (totLumi>lumiThreshold):
        ite=ite+1
        lastRun = aRun[0]
        print ite, firstRun, lastRun, totLumi
        createFile(ite, firstRun, lastRun)
        totLumi = 0
    if (aRun==listRuns[-1]):
        ite=ite+1
        lastRun = aRun[0]
        print ite, firstRun, lastRun, totLumi
        createFile(ite, firstRun, lastRun)









import json,sys

debug = True

sample = {u'eegPower': {u'lowGamma': 2977, u'highGamma': 970, u'highAlpha': 11293, u'delta': 295753, u'highBeta': 5279, u'lowAlpha': 2267, u'lowBeta': 5814, u'theta': 13820}, u'poorSignalLevel': 0, u'eSense': {u'meditation': 84, u'attention': 74}}


def printCSVLine(record,header = False,detailed=False):
    #columns = ['lowAlpha','highAlpha','lowBeta','highBeta','lowGamma',"highGamma","delta","theta","meditation","attention"]
    columns = []
    if detailed:
        columns = ["user","startTime","sampleNum"]
    
    columns = columns + ['lowAlpha','highAlpha','lowBeta','highBeta','lowGamma',"highGamma","delta","theta"]
    if header:
        return ",".join(columns) + "\n"

    if len(record) == 0:
        return ""

    writeList = [ str(record[col]) for col in columns ]
    return ",".join(writeList) + "\n"


def convertEsenseToCsv(filename,merge=False):
    fin = open(filename,"rU")

    if merge:
        outfilename = "data.csv"
    else:
        outfilename = filename+".csv"

    fout = open(outfilename,"a")
    
    filenameTokens = filename.split(".")[0].split(" ")
    user = filenameTokens[0]
    startTime = " ".join(filenameTokens[2:])


    if not merge: fout.write(printCSVLine({},True,merge))
    sampleNum = 0

    for line in fin:
        line = line.strip()
        if len(line) == 0:
            continue

        result = {}
        if debug: print filename,line
        lineDict = json.loads(line)
        if debug: print lineDict
                   
        if 'eegPower' in lineDict:
            result.update(lineDict['eegPower'])
        if 'eSense' in lineDict:
            result.update(lineDict['eSense'])
        if 'poorSignalLevel' in lineDict:
            result['poorSignalLevel'] = lineDict['poorSignalLevel']

        if merge and len(result) > 0:
            result['user'] = user
            result['startTime'] = startTime
            result['sampleNum'] = sampleNum
            sampleNum += 1

        fout.write(printCSVLine(result,detailed=merge))



if __name__ == "__main__":
    sys.argv = sys.argv[1:]
    for filename in sys.argv:
        convertEsenseToCsv(filename,True)

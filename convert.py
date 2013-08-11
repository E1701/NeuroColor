import json,sys

debug = 0

sample = {u'eegPower': {u'lowGamma': 2977, u'highGamma': 970, u'highAlpha': 11293, u'delta': 295753, u'highBeta': 5279, u'lowAlpha': 2267, u'lowBeta': 5814, u'theta': 13820}, u'poorSignalLevel': 0, u'eSense': {u'meditation': 84, u'attention': 74}}


def printCSVLine(record,outfile,header = False):
    #columns = ['lowAlpha','highAlpha','lowBeta','highBeta','lowGamma',"highGamma","delta","theta","meditation","attention"]
    columns = ['lowAlpha','highAlpha','lowBeta','highBeta','lowGamma',"highGamma","delta","theta"]
    if header:
        outfile.write(",".join(columns))
        outfile.write("\n")

    if len(record) == 0:
        return

    writeList = [ str(record[col]) for col in columns ]
    outfile.write(",".join(writeList))
    outfile.write("\n")


def convertEsenseToCsv(filename):
    fin = open(filename,"rU")
    fout = open(filename+".csv","w")
    printCSVLine({},fout,True)

    for line in fin:
        line = line.strip()
        if len(line) == 0:
            continue
        if debug: print line
        lineDict = json.loads(line)
        if debug: print lineDict
        result = {}
        if 'eegPower' in lineDict:
            result.update(lineDict['eegPower'])
        if 'eSense' in lineDict:
            result.update(lineDict['eSense'])
        if 'poorSignalLevel' in lineDict:
            result['poorSignalLevel'] = lineDict['poorSignalLevel']

        printCSVLine(result,fout)



if __name__ == "__main__":
    sys.argv = sys.argv[1:]
    for filename in sys.argv:
        convertEsenseToCsv(filename)

import os
import datetime

def ProcessOneFile(FileHandler, outHandler):
    FileHandler.readline()
    OneLine = FileHandler.readline()

    Splitted = OneLine.split()
    pastdate = datetime.datetime.strptime(Splitted[-1], '%d-%m-%Y').year
    ret = []
    temp = float(Splitted[0])
    tempcount = 1
    for OneLine in FileHandler:
        Splitted = OneLine.split()
        date = datetime.datetime.strptime(Splitted[-1], '%d-%m-%Y')
        if ( ( date.year - pastdate ) > 1):
            ret.append([pastdate, temp/tempcount])
            temp = float(Splitted[0])
            tempcount = 1
            pastdate = date.year
        else:
            temp += float(Splitted[0])
            tempcount += 1
    ret.append([pastdate, temp/tempcount])

    for OneThing in ret:
        outHandler.write( str(OneThing[0])+'\t'+str(OneThing[1]) + '\n')


def ProcessDirectory(dir):
    file = open('out.txt', 'w')
    files = os.listdir(dir)
    for OneItem in files:
        if (os.path.isdir( os.path.join(dir, OneItem))):
            ProcessDirectory(os.path.join(dir, OneItem))
        else:
            if (OneItem.split('.')[-1] == 'tim'):
                ThisFile = open( os.path.join(dir, OneItem), 'r')
                print(OneItem)
                ProcessOneFile(ThisFile, file)
                ThisFile.close()
    file.close()

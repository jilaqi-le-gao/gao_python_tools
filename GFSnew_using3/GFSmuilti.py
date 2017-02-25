import os
import datetime
import time
import GFSnew_using3.GenerateFile as GenerateFile
import subprocess
from multiprocessing import Pool


#file name list
TobeDownload = []
TargetName = []
urlHead = 'http://www.ftp.ncep.noaa.gov/data/nccf/com/gfs/prod/gfs.'

def OneSingleDownload(TargetPath, url, TargetName):
    """

    :param TargetPath:
    :param url:
    :param TargetName:
    :return:
    """
    command = 'wget -c -nv -P '+TargetPath+' '+url+ ' -O ' + TargetName
    returncode = 100
    while (returncode != 0):
        thisprocess = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        returncode = thisprocess.wait()


def StartDownload(Date, UTC, ForecastHour, DataType, TargetDir):
    """

    :param date:
    :param UTC:
    :param ForecastHour:
    :param DataType:
    :param TargetDir:
    :return:
    """
    global TobeDownload, TargetName
    [TobeDownload , TargetName] = GenerateFile.GetSourceTarget(Date, UTC, ForecastHour, DataType)

    urlH = urlHead + Date.strftime('%Y%m%d')+'%02d'%UTC

    multiple_results=[]
    with Pool(processes=1) as pool:
        for (i, OneName) in enumerate(TobeDownload):
            url = urlH + '/' + OneName
            multiple_results.append(pool.apply_async(os.getpid(),()))#OneSingleDownload, (TargetDir, url, TargetName[i]))

        print([res.get(timeout=1) for res in multiple_results])



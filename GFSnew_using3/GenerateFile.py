import datetime

gfsSource = {
    'gfs3': 'gfs.t%02dz.pgrb2.1p00.f%03d',
    'gfs4': 'gfs.t%02dz.pgrb2.0p50.f%03d',
    'gfs5': 'gfs.t%02dz.pgrb2.0p25.f%03d'
}

gfsTarget = {
    'gfs3': '_fh.%04d_tl.presss.gr.1p0deg.grib2',
    'gfs4': '_fh.%04d_tl.presss.gr.0p5deg.grib2',
    'gfs5': '_fh.%04d_tl.presss.gr.0p2deg.grib2'
}

def GetSourceTarget(Date, UTC, ForecastHour, DataType):
    """

    :param Date:
    :param UTC:
    :param ForecastHour:
    :param Datatype:
    :return:
    """
    SourceFileNames = []
    TargetFileNames = []

    DateString = Date.strftime('%Y%m%d') + '%02d'%UTC
    Source = gfsSource[DataType]
    Target = DateString+gfsTarget[DataType]

    for hour in range(0, ForecastHour+1, 1):

        SourceFileNames.append(Source%(UTC, hour))
        TargetFileNames.append(Target%(hour))

    return SourceFileNames, TargetFileNames
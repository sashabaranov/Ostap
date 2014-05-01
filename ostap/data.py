import ROOT
from AnalysisPython.GetLumi import getLumi

class Data(object):
    """
    Contains data info inside.
    """

    def __init__(self,
                branch,
                files=[]):
        self.data = ROOT.TChain(branch)
        self.filelist = []

        if files:
            self.add_files(files)

    def add_files(self, files):
        self.filelist += files

        for f in files:
            self.data.Add(f)

    def __str__(self):
        ret = "<#files: {}; Entries: {}>".format(len(self.filelist), len(self.data))

        return ret


class DataAndLumi(object):
    """
    Contains data and luminosity info inside.
    """

    def __init__(self,
                branch,
                lumi_branch='GetIntegratedLuminosity/LumiTuple',
                files=[]):
        self.data = ROOT.TChain(branch)
        self.lumi = ROOT.TChain(lumi_branch)
        self.filelist = []

        if files:
            self.add_files(files)

    def add_files(self, files):
        self.filelist += files

        for f in files:
            self.data.Add(f)
            self.lumi.Add(f)

    def get_luminosity(self):
        return getLumi(self.lumi)

    def __str__(self):
        ret = "<"
        ret += "Luminosity: {}; #files: {}; ".format(self.get_luminosity(), len(self.filelist))
        ret += "Entries: {}>".format(len(self.data))

        return ret

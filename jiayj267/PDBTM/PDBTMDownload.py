# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------------------
# @file:        PDBTMdatabasefile
# @Author:      JYJ
# @Purpose:
# @Created:     2018/2/11
# @update:      2018/2/11
# @Software:    PyCharm
# -------------------------------------------------------------------------------
import urllib

class PDBTMDownload():

    def __init__(self):
        """Constructor"""


    def getWebPage(self, url, databasepath):
        try:
            """
            urlretrieve() will download the url location page to the temporary file
            """
            revtal = urllib.request.urlretrieve(url)[0]
            filepath = databasepath
        except IOError:
            revtal = None
        if revtal:      #Handle it when the reval is not empty
            self.saveWebPage(revtal, filepath)

    def saveWebPage(self, webpage, path):
        """
        Saving the downloaded page to the xmlfile
        """
        f = open(webpage)  #Open the temporary file you downloaded.
        lines = f.readlines()
        f.close()
        fobj = open(path, 'w')
        fobj.writelines(lines)
        fobj.close()

# def main():
#
#     pdbtmdownload = PDBTMDownload()
#     pdbtmdownload.getWebPage('http://pdbtm.enzim.hu/data/pdbtmall', 'C:/Users/jiayj/Desktop/pdbtm.xml')
#
# if __name__ == '__main__':
#     main()
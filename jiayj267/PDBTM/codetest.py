# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------------------
# @file:
# @Author:      JYJ
# @Purpose:     Test the PDBTMDownload.py and the PDBTMParse.py
# @Created:     2018/3/14
# @update:
# @Software:    PyCharm
# -------------------------------------------------------------------------------

from PDBTMDownload import PDBTMDownload
from PDBTMParse import PDBTMParse

def main():
    pdbtmdownload = PDBTMDownload()
    pdbtmdownload.getWebPage('http://pdbtm.enzim.hu/data/pdbtmall', 'C:/Users/jiayj/Desktop/pdbtm.xml')
    pdbtm = PDBTMParse()
    pdbtm.pdbtmparse('C:/Users/jiayj/Desktop/pdbtmall.xml')

if __name__ == '__main__':
    main()

# main()中需按照实际存储位置更改数据库文件的存放地址
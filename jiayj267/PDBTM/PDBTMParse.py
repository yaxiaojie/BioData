# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------------------
# @file:        PDBTMfile
# @Author:      JYJ
# @Purpose:
# @Created:     2018/1/28
# @update:      2018/1/30
# @Software:    PyCharm
# -------------------------------------------------------------------------------
end = []
import DS
import string
class PDBTMParse():

    def __init__(self):
        '''

        '''

    def pdbtmparse(self, path):
        with open(path, "r") as files:
            lines = files.readlines()
            end.append(0)
            for i in range(len(lines)):
                if lines[i].startswith('</pdbtm>'):
                    end.append(i)
            for j in range(len(end)-1):
                pdbtm_dic = {}
                pdbtm_list = []
                for z in range(end[j], end[j+1]):
                    if lines[z].startswith('<pdbtm '):
                        pdbtmid = (lines[z].split(" ")[-2])[-5:-1]
                        pdbtm_dic[pdbtmid] = pdbtm_list
                    if lines[z].startswith('  <CREATE_DATE>'):
                        create_date_dic = {}
                        create_date = (lines[z].split(">")[1]).split("<")[0]
                        create_date_dic['CREATE_DATE'] = create_date
                        pdbtm_list.append(create_date_dic)
                    elif lines[z].startswith('  <MODIFICATION>'):
                        modification_list = []
                        modification_dic = {}
                        if lines[z + 1].startswith('    <DATE>') and lines[z + 2].startswith('    <DESCR>'):
                            date_dic = {}
                            descr_dic = {}
                            date = (lines[z + 1].split(">")[1]).split("<")[0]
                            descr = (lines[z + 2].split(">")[1]).split("<")[0]
                            date_dic['DATE'] = date
                            descr_dic['DESCR'] = descr
                            modification_list.append(date_dic)
                            modification_list.append(descr_dic)
                            modification_dic['MODIFICATION'] = modification_list
                            pdbtm_list.append(modification_dic)
                    elif lines[z].startswith('  <RAWRES>'):
                        rawres_dic = {}
                        rawres_list = []
                        rawres_dic['RAWRES'] = rawres_list
                        pdbtm_list.append(rawres_dic)
                    elif lines[z].startswith('    <TMRES>'):
                        tmares_dic = {}
                        tmares = (lines[z].split(">")[1]).split("<")[0]
                        tmares_dic['TMRES'] = tmares
                        rawres_list.append(tmares_dic)
                    elif lines[z].startswith('    <TMTYPE>'):
                        tmtype_dic = {}
                        tmtype = (lines[z].split(">")[1]).split("<")[0]
                        tmtype_dic['TMTYPE'] = tmtype
                        rawres_list.append(tmtype_dic)
                    elif lines[z].startswith('    <SPRES>'):
                        spres_dic = {}
                        spres = (lines[z].split(">")[1]).split("<")[0]
                        spres_dic['SPRES'] = spres
                        rawres_list.append(spres_dic)
                    elif lines[z].startswith('    <PDBKWRES>'):
                        pdbkwres_dic = {}
                        pdbkwres = (lines[z].split(">")[1]).split("<")[0]
                        pdbkwres_dic['PDBKWRES'] = pdbkwres
                        rawres_list.append(pdbkwres_dic)
                    elif lines[z].startswith('    <PDBKWORD>'):
                        pdbkword_dic = {}
                        pdbkword = (lines[z].split(">")[1]).split("<")[0]
                        pdbkword_dic['PDBKWORD'] = pdbkword
                        rawres_list.append(pdbkword_dic)
                    elif lines[z].startswith('  <MEMBRANE>'):
                        membrane_dic = {}
                        membrane_list = []
                        membrane_dic['MEMBRANE'] = membrane_list
                        pdbtm_list.append(membrane_dic)
                        if lines[z+1].startswith('    <NORMAL'):
                            normal_dic = {}
                            normal_list = []
                            normal_list.append((lines[z+1].split("L ")[1]).split("/")[0])
                            normal_dic['NORMAL'] = normal_list
                            membrane_list.append(normal_dic)
                            # print(normal_dic)
                        if lines[z+2].startswith('    <TMATRIX>'):
                            tmatrix_dic = {}
                            tmares_list =[]
                            rowx_dic = {}
                            rowy_dic = {}
                            rowz_dic = {}
                            rowx_dic['ROWX'] = (lines[z+3].split("X ")[1]).split("/")[0]
                            rowy_dic['ROWY'] = (lines[z+4].split("Y ")[1]).split("/")[0]
                            rowz_dic['ROWZ'] = (lines[z+5].split("Z ")[1]).split("/")[0]
                            tmares_list.append(rowx_dic)
                            tmares_list.append(rowy_dic)
                            tmares_list.append(rowz_dic)
                            tmatrix_dic['TMATRIX'] = tmares_list
                            membrane_list.append(tmatrix_dic)
                    elif lines[z].startswith('  <SIDEDEFINITION'):
                        sidedefinition_dic = {}
                        sidedefinition_list = []
                        note_dic = {}
                        sidedefinition_list.append((lines[z].split("N ")[1]).split(">")[0])
                        note_dic['NOTE'] = (lines[z+1].split("<NOTE>")[1]).split("<")[0]
                        sidedefinition_list.append(note_dic)
                        sidedefinition_dic['SIDEDEFINITION'] = sidedefinition_list
                        pdbtm_list.append(sidedefinition_dic)
                    elif lines[z].startswith('  <BIOMATRIX>'):
                        biomatrix_dic = {}
                        biomatrix_list = []
                        biomatrix_dic['BIOMATRIX'] = biomatrix_list
                        pdbtm_list.append(biomatrix_dic)
                    elif lines[z].startswith('    <MATRIX '):
                        matrix_dic = {}
                        matrix_list = []
                        matrixid = lines[z].split('"')[1]
                        matrix_dic[matrixid] = matrix_list
                        biomatrix_list.append(matrix_dic)
                    elif lines[z].startswith('      <APPLY_TO_CHAIN'):
                        apply_to_chain_dic = {}
                        apply_to_chain_dic['APPLY_TO_CHAIN'] = (lines[z].split('<APPLY_TO_CHAIN ')[1]).split('/')[0]
                        matrix_list.append(apply_to_chain_dic)
                    elif lines[z].startswith('      <TMATRIX>'):
                        tmatrix_list2 = []
                        tmatrix_dic2 = {}
                        rowx_dic2 = {}
                        rowy_dic2 = {}
                        rowz_dic2 = {}
                        rowx_dic2['ROWX'] = (lines[z + 1].split("X ")[1]).split("/")[0]
                        rowy_dic2['ROWY'] = (lines[z + 2].split("Y ")[1]).split("/")[0]
                        rowz_dic2['ROWZ'] = (lines[z + 3].split("Z ")[1]).split("/")[0]
                        tmatrix_list2.append(rowx_dic2)
                        tmatrix_list2.append(rowy_dic2)
                        tmatrix_list2.append(rowz_dic2)
                        tmatrix_dic2['TMATRIX'] = tmatrix_list2
                        matrix_list.append(tmatrix_dic2)
                    elif lines[z].startswith('    <DELETE '):
                        delete_dic = {}
                        delete_dic['DELETE'] = (lines[z].split('<DELETE ')[1]).split('/')[0]
                        biomatrix_list.append(delete_dic)
                    elif lines[z].startswith('  <CHAIN'):
                        chain_dic = {}
                        chain_list = []
                        chain_list.append((lines[z].split('<CHAIN ')[1]).split('\n')[0])
                        chain_dic['CHAIN'] = chain_list
                        pdbtm_list.append(chain_dic)
                    elif lines[z].startswith('    <SEQ>'):
                        seq_dic = {}
                        seq_list = []
                        seq = ''
                        for m in range(1, 30):
                            if lines[z+m].startswith('    </SEQ>'):
                                break
                            else:
                               seq += (lines[z + m].lstrip()).split('\n')[0]
                        seq_list.append(seq)
                        seq_dic['SEQ'] = seq_list
                        chain_list.append(seq_dic)
                    elif lines[z].startswith('    <REGION '):
                        region_dic = {}
                        region_dic['REGION'] = (lines[z].split('    <REGION ')[1]).split('/')[0]
                        chain_list.append(region_dic)
                # return pdbtm_dic
                a = DS.DataStorage('PDBTM')
                a.Storage(pdbtm_dic)

# def main():
#     pdbtm = PDBTMParse()
#     pdbtm.pdbtmparse('C:/Users/jiayj/Desktop/pdbtmall.xml')
#
# if __name__ == '__main__':
#     main()
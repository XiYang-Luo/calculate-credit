# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:45:53 2018

@author: luo xi yang
"""

"""
该部分使用主函数给出的文件路径，输出必修、限选、任选、实践四门性质课程的列表。及时，
每一门该性质的课程对应的学分列表。最终返回为元组形式。
"""
import pyexcel_io
import pyexcel_xls
#from pyexcel_xls import get_data  
#from pyexcel_xls import save_data  #使用pyexcel_xls读取excel表信息
 
class Openfile():
    def __init__(self,path):
        self.path=path
        
    def contents_of_file(self):
        xls_data = pyexcel_xls.get_data(self.path)  #或者使用get_data(r"学分.xlsx") 
        #print("Get data type:", type(xls_data))
        ai=[]
        for i in xls_data.values():  
            #print(i)
            ai.append(i)
        #ai=np.array(ai)
        data=[]
        for j in ai:
            print('该文件有这么多行:\n',str(len(j)))
            for i in range(0,len(j)):
                #print('\n\n',str(j[i]))
                data.append(j[i])
        #print(data)
        compulsory,limited_selection,optional,practice=[],[],[],[]
        for i in range(1,len(data)):
            if '必修' in data[i]:
                compulsory.append(data[i][5])
                #print('测试，必修\n',str(data[i][5]))
            elif '限选' in data[i]:
                #print('测试，限选\n',str(data[i][5]))
                limited_selection.append(data[i][5])
            elif '任选' in data[i] or '选修' in data[i]:
                #print('测试，任选\n',str(data[i][5]))
                optional.append(data[i][5])
            elif '实践' in data[i]:
                #print('测试，实践\n',str(data[i][5]))
                practice.append(data[i][5])
            else:
                print('Woring!!!  Mismatch of content!\n')
        return compulsory,limited_selection,optional,practice

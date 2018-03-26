# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:07:11 2018

@author: luo xi yang
"""
"""
该部分用于求和计算
"""
class CountContents():
    def __init__(self,selection):
        self.selection=selection
    
    def tempcount(self):
        count1=self.selection
        #print('检测，必修：\n',str(count1))
        summ=0
        for i in count1:
            summ+=i
        #print(summ)
        return summ

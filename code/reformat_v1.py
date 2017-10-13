#!/usr/bin/python
###########################################################################################################################
# reformat.py version 1.0
# Python 2.7.6
# author: minjeong kim
# This code modifies the format of the ped file.
# * command example : python reformat.py chrN.ped
# output : re_chrN.ped
# The modified ped format is as follows.
# Before) sampleID_sampleID sampleID_sampleID 0 0 0 -9 A A C C T T G G A A A A ......
# * After) sampleID     A A     C C     T T     G G     A A     A A    ......
###########################################################################################################################
import sys
print('################## reformat v1.0 ###################')
var = sys.argv[1]
input = open(var,'r')   # Open the chrN.ped
output = open('re_'+var,'w+')
text = input.readlines()
for line in text:
    arr =line.split(' ')
    for i in range(len(arr)):
        if i == 0 :
            sampleID = arr[0].split('_')
            sampleID = sampleID[0]
            output.write(sampleID+'\t')
        elif i > 5 :
            if i%2==0 :
                output.write(arr[i]+' ')
            else :
                if i == len(arr)-1 :
                    output.write(arr[i])
                else : 
                    output.write(arr[i]+'\t')
    print(sampleID+' finish.')
print('')
print('* New file : re_'+var)
input.close()
output.close()

###########################################################################################################################
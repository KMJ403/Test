#!/usr/bin/python
input = open('Genome_Care.vcf','r')
output = open('Genome_care_ch1.vcf','w+')
text = input.readlines()
for line in text:
	arr =line.split()
	if arr[0]=='1' :
		output.write(line)
	elif arr[0]=='2' :
		break
	else :
		output.write(line)
input.close()
output.close()

#!/usr/bin/pythonw

import sys
import string
from sets import Set
import re
from operator import itemgetter


# Files, Input and Output
# Get files names from command line:

#print 'Number of Argv:', len(sys.argv), 'files'
#print 'Usage:', sys.argv

print 'Input File name:', sys.argv[-3]
print 'Output File name:', sys.argv[-2]

#######################################################################################################################################
Threshold = int(sys.argv[-1]) #100
#######################################################################################################################################
print 'Thresold:'+str(Threshold)

# LOADING THE FILES
print 'LoadingData'
#Table2_1file = open('Table2_1.txt','r')
Table2_1file = open(sys.argv[-3],'r')

#TableSort3_1file = open('TableSort3_1.txt','w')
Table3_1file = open(sys.argv[-2],'w')


######################################################################################################################################

# SORTING INDELS BY POSITION

linedata = []
matrix = []

count = 0

dataline = [1,2,3]

print 'SortingData'

for line in Table2_1file.readlines():                 # reads line by line on the input file
   a = line.rstrip()                                  # removing whitespaces
   b=a.replace('\t\t','\t')                           # replacing double tab by one tab
   linedata.append(b.split('\n'))                     # append method call; add one item at the end; then split characteres by a new line

   if count > 0:
     aux = (linedata[count][0].split('\t'))
     if aux[2] != '?':
        pos = aux[2]
        rs = aux[0].strip()
        allele = aux[1].replace("'","")
        matrix.append([rs.strip(),allele.strip(),int(pos)])

   else:
      header=(linedata[count][0].split('\t'))

   count =count+1

#print('\nTable2 end\n')
#print(linedata)
#print('\n')

#for aux in matrix:
#   print (aux)

#print('\n')

#-----------
def getKey(item):
   return item[2]
matrix2 = sorted(matrix, key=getKey)
#-----------

#print header
#for aux2 in matrix2:
#   print (aux2)

######################################################################################################################################

# SEPARATE INDELS IN GROUPS ACCORDING TO THRESHOLD VALUE (100) AND ALLELE LENGTH

matrix2len = len(matrix2[1])  #number of columns
matrix2size = len(matrix2)    # number of rows
# (matrix2 [Line])[Column] -- accessing item

group_n = 1
count1 = 0
Group = []
count2 = 0
groupadd = 0

while(count1<matrix2size):
   count2 = count1 + 1

   while (count2<matrix2size):

      #inside thresold?
      if ( ((matrix2[count2])[2] - (matrix2[count1])[2]) <= Threshold):

         # same allele lenght?
          if ( (len((matrix2[count2])[1])) == (len((matrix2[count1])[1])) ):
                groupadd = 1   #flag to define that at least one pair is added to the group
                pair = str(group_n)+'\t'+str( (matrix2[count1])[0] ) +'\t'+ str( (matrix2[count2])[0] )+'\t'+( (matrix2[count1])[1] )+'\t'+( (matrix2[count2])[1] )+'\t'+str( (matrix2[count1])[2] )+'\t'+str( (matrix2[count2])[2] )
                print pair
                Group.append(pair)
      else:
          count2 = matrix2size

      count2 = count2 + 1

   if (groupadd == 1):
      group_n = group_n + 1
      groupadd = 0

   count1 = count1 + 1

print 'SavingPairs'
#print Group

# Saving Data and closing Files

Table3_1file.write('Group        ')
Table3_1file.write('\t')
Table3_1file.write('rsIDs        ')
Table3_1file.write('\t')
Table3_1file.write('Allels       ')
Table3_1file.write('\t')
Table3_1file.write('Positions')
Table3_1file.write('\n')


count = 0
while count<(len(Group)):
   Table3_1file.write( Group[count] )
   Table3_1file.write('\n')
   count = count + 1

Table2_1file.close()
Table3_1file.close()

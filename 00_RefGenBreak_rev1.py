#!/usr/bin/pythonw

import sys
import string
from sets import Set
import re
from operator import itemgetter

#######################################################################################################################################
class BreakFile:

   def __init__(self):
      self.refseq = ''

   def LoadRef(self,file):
      # refsequence_Chr1_GRCh37p13_test.fasta
      # Genome --> 70 characters per line

      RefGenomeHandler = open(file, 'r')     # Open Genome Reference File

      count_line = 0
      self.refseq = ''
      for Fragline in RefGenomeHandler.readlines():
         if count_line > 0:
            self.refseq = self.refseq + Fragline
         if ( (count_line%10000) == 0 ):
            print count_line
         count_line = count_line + 1

      RefGenomeHandler.close()
      #print self.refseq

   def Break(self,file,nlines):
      # refsequence_Chr1_GRCh37p13_test.fasta
      # Genome --> 70 characters per line

      self.RefGenomeHandler = open(file, 'r')     # Open Genome Reference File

      currlines = nlines
      linesgroup = 0
      flag_line1 = 0
      lastLine = ''
      last_1 = ''


      for Fragline in self.RefGenomeHandler.readlines():

#         print str(int(currlines/nlines))+' - '+str(currlines)
         if flag_line1 > 0:
            if (int(currlines/nlines)>0):
               currlines = 0
               linesgroup = linesgroup + 1
               RefGenomeHandler = open('\Users\Sasan Najar\HomeDir\project\refsequence_Chr5_GRCh37p13'+str(linesgroup)+'.fasta', 'w')     # Open Genome Reference File
               aux = str((currlines+(linesgroup-1)*nlines)-1)
               if (int(aux)<1):
                  aux = '1'
               RefGenomeHandler.write( aux + '\t' + str( (linesgroup)*nlines ) + '\n')

               if (last_1!=''):
#                  aux = str((currlines+(linesgroup-1)*nlines)-1)+'\t'+last_1
                  aux = last_1
                  RefGenomeHandler.write(aux)

               if (lastLine!=''):
#                  aux = str((currlines+(linesgroup-1)*nlines))+'\t'+lastLine
                  aux = lastLine
                  RefGenomeHandler.write(aux)


            currlines = currlines + 1
#            aux = (str(currlines+(linesgroup-1)*nlines)+'\t'+Fragline)
            aux = (Fragline)
            RefGenomeHandler.write(aux)

            last_1 = lastLine
            lastLine = Fragline

         flag_line1 = 1


 #     RefGenomeHandler.close()

#######################################################################################################################################
# MAIN #
#######################################################################################################################################
File = sys.argv[-2]
Num = sys.argv[-1]
#######################################################################################################################################
print ' File         : ', File
print ' Break Number : ', Num
#######################################################################################################################################

Result = BreakFile()

Result.Break(File,int(Num))
#Result.LoadRef(File)

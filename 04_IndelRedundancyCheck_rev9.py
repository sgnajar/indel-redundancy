#!/usr/bin/pythonw

import sys
import string
from sets import Set
import re
from operator import itemgetter

#######################################################################################################################################
class Redundancy:
   def __init__(self,fileGroup,IndelType):
      self.frag = ''
      self.currgroup = 1
      self.currlinegr = 0
      self.fileGroupName = fileGroup
      self.Type = IndelType
      self.groups = []
      self.start = 0
      self.end = 0
      self.fragstart = 0
      self.fragend = 0
      self.refGenline = 0
      self.startfragline = 0
      self.endfragline = 0
      self.Table4 = []
   
   def LoadGroupfile(self):

      self.GroupHandler = open(self.fileGroupName, 'r')          # Open Group File
      countG = 0   # number of lines on the group
      for Groupline in self.GroupHandler.readlines():
         if(countG>0):
            aux1 = Groupline.replace('\n','')
            aux2 = aux1.split('\t')
            aux2[0] = int(aux2[0])
            aux2[6] = int(aux2[6])                                # position provided as string, changed to number
            aux2[5] = int(aux2[5])                                #
            aux2[4] = aux2[4].replace('-/','')                    #remove not used character attached to alleles
            aux2[3] = aux2[3].replace('-/','')                    #
            self.groups.append(aux2)
         countG = countG + 1

      #print self.groups

                                                                    
      self.GroupHandler.close()

   def Range(self):  #return the range for the next group

      # looking for the first group element
      FirstGrElement =  self.currlinegr

      while (self.groups[FirstGrElement])[0]<self.currgroup:
         FirstGrElement = FirstGrElement + 1
      # FirstGrElement = FirstGrElement - 1 # back to the first element
         

      self.currlinegr = FirstGrElement             #save the first line of the group
      
      # looking for the Last group element
      LastGrElement = FirstGrElement

      lastline = False
      maxGroupLines = len(Result.groups)
      while ( ( (self.groups[LastGrElement])[0]<=self.currgroup) and (lastline == False) ):
          LastGrElement = LastGrElement + 1

          # checking if it is the last group
          if LastGrElement>= (maxGroupLines):
             LastGrElement = LastGrElement - 1
             lastline = True
             print 'Lastline:'+str(lastline)
             break

      if (lastline == False):   
         LastGrElement = LastGrElement - 1

      # define start and end position of the fragment to be extracted
      start = (self.groups[FirstGrElement])[5] - 5               
      end   = (self.groups[LastGrElement ])[6] + 50     

      return [start,end,lastline]
      
   def AdvanceGroup(self):    
      self.currgroup = self.currgroup + 1

   def CreatingVarDel(self,startPos,Allele1):
         # startPos  - Deletion Start Position
         # Allele1   - Alllele Deletion

         flag_deletion = 0
         relstart1 = startPos - self.startfile + 1
         pos = 0
         sample = ''
         for base in self.frag:
            pos=pos+1

            if flag_deletion == 0:
               # find the postion for deletion
               if(pos==relstart1):
                  #print 'Found Pos: '+str(pos)+'-'+str(startPos)+'\n'
                  #sample = sample + '\t\t\t\t\t\t\t\t\t'
                  flag_deletion = 1
                  allelesize = len(Allele1)
                  allelecount = 0
                  #do the deletion
               else:
                  sample = sample + base   #sample -- modified fragment

            if flag_deletion == 1:
               
               if Allele1[allelecount] != base: # reference Genome element to delete != than Allele notation
                  return False               
               allelecount = allelecount+1
               if allelecount==allelesize:
                  flag_deletion = 0

         return sample

   def CreatingVarIns(self,startPos,Allele1):
         # startPos  - Deletion Start Position
         # Allele1   - Alllele Deletion

         relstart1 = startPos - self.startfile + 1
         pos = 0
         sample = ''
         for base in self.frag:
            pos=pos+1
            if(pos==relstart1):
                  sample = sample + Allele1

            sample = sample + base   #sample -- modified fragment
  
         return sample

   def RedCandidates(self):
      # self.currgroup     -- Groupd number
      # self.currlinegr    -- first group line
      # self.startfile     -- first postion onn the fragment
      # self.endfile       -- end postion on the fragment
      # self.frag          -- fragment
      # self.groups        -- groups matrix
      #    [0]             -- group number
      #    [1]             -- rs1
      #    [2]             -- rs2
      #    [3]             -- Allele1
      #    [4]             -- Allele2
      #    [5]             -- pos1
      #    [6]             -- pos2
      # self.Table4_1           -- Output table with redundance check included

      printflag = 1
      
      # looking for the first group element
      GrElement =  self.currlinegr
      allelesize = 0
      allelecount = 0

      ############################ make allele variant 1
      #print 'Base Group Sample:'
      if (self.Type == 'D'):
         sample1 = self.CreatingVarDel((self.groups[GrElement])[5],(self.groups[GrElement])[3])
      else:
         sample1 = self.CreatingVarIns((self.groups[GrElement])[5],(self.groups[GrElement])[3])

      maxGroupLines = len(Result.groups)
      while (self.groups[GrElement])[0]<=self.currgroup:


         #print str((self.groups[GrElement])[0])+' '+str((self.groups[GrElement])[1])+' '+str((self.groups[GrElement])[2])+' '+str((self.groups[GrElement])[3])+' '+str((self.groups[GrElement])[4])+' '+str((self.groups[GrElement])[5])+' '+str((self.groups[GrElement])[6])+' '          

         ########################### make alelle variant 2
         if (self.Type == 'D'):
            sample2 = self.CreatingVarDel((self.groups[GrElement])[6],(self.groups[GrElement])[4])
         else:
            sample2 = self.CreatingVarIns((self.groups[GrElement])[6],(self.groups[GrElement])[4])

         # compare var1 and var2
         if (sample1 == sample2): # save Y on output Table

#            if(self.Type == 'D'):
#               self.Table4.append( [(self.groups[GrElement])[0],(self.groups[GrElement])[1],(self.groups[GrElement])[2],(self.groups[GrElement])[3],(self.groups[GrElement])[4],(self.groups[GrElement])[5],(self.groups[GrElement])[6],'Y'] )
#            else:  # if it is not deleltion it is insertion
            self.Table4.append( [(self.groups[GrElement])[0],(self.groups[GrElement])[1],(self.groups[GrElement])[2],(self.groups[GrElement])[3],(self.groups[GrElement])[4],(self.groups[GrElement])[5],(self.groups[GrElement])[6],'Y'] )
               
            #print str((self.groups[GrElement])[0])+' '+str((self.groups[GrElement])[1])+' '+str((self.groups[GrElement])[2])+' '+str((self.groups[GrElement])[3])+' '+str((self.groups[GrElement])[4])+' '+str((self.groups[GrElement])[5])+' '+str((self.groups[GrElement])[6])+' '          
            
         else:
#            if(self.Type == 'D'):
#               self.Table4.append( [(self.groups[GrElement])[0],(self.groups[GrElement])[1],(self.groups[GrElement])[2],(self.groups[GrElement])[3],(self.groups[GrElement])[4],(self.groups[GrElement])[5],(self.groups[GrElement])[6],'_'] )
#            else: # if it is not deleltion it is insertion
            self.Table4.append( [(self.groups[GrElement])[0],(self.groups[GrElement])[1],(self.groups[GrElement])[2],(self.groups[GrElement])[3],(self.groups[GrElement])[4],(self.groups[GrElement])[5],(self.groups[GrElement])[6],'_'] )
             
         
         GrElement = GrElement + 1
         # checking if it is the last group
         if GrElement>= (maxGroupLines):
              break


   def ExtractFragment(self,start,end):
      # refsequence_Chr1_GRCh37p13_test.fasta
      # Genome --> 70 characters per line 
      # endfragline   = int(end/70)   --> fragend = endfragline*70
      # First line = 1

      #define the file to load
      Filesize = 10000*70                                   #  number of lines in a file * number of positions per line
      Overlap = 140                                         #  overlap = two extra lines on the file before, must be bigger than thresold
      FileNumberStart = int((start+Overlap)/Filesize)+1
      FileNumberEnd   = int((end+Overlap)/Filesize)+1

      # Check if Block is too big
      out = True
      if (FileNumberStart!=FileNumberEnd):
         out = False

      # open the selected File
      fileRefGenName = 'Users\Sasan Najar\HomeDir\project\refsequence_Chr5_GRCh37p13'+str(FileNumberEnd)+'.fasta'
      RefGenomeHandler = open(fileRefGenName, 'r')     # Open Genome Reference File

      #Load the File string, self.frag is the string file, self.startfile is the start position an self.endfile is the end position
      count_line = 0
      self.frag = ''
      for Fragline in RefGenomeHandler.readlines():
         count_line = count_line + 1      
         
         if count_line == 1:
            aux = Fragline.replace('/n','')
            aux = aux.split('\t')
            self.startfile =  int(aux[0])*70-69  #getting first position on the line
            self.endfile =  int(aux[1])*70

         else:  #removing Hader with positions
            self.frag = self.frag + Fragline.replace('\n','')           

      #print 'RefSeqfile'+str(FileNumberStart)
      #print 'Start:'+str(self.startfile)
      #print 'End  :'+str(self.endfile)
      #print self.frag
      RefGenomeHandler.close()
      return out
         
#######################################################################################################################################
# MAIN #
#######################################################################################################################################
print '\n\n\n Indel Type    : '+str(sys.argv[-3])
print ' Input File    : '+str(sys.argv[-2])
print ' Output File   : '+str(sys.argv[-1])+'\n'
#######################################################################################################################################
IndelType = sys.argv[-3]
Infile   = sys.argv[-2]
Outfile    = sys.argv[-1]
#######################################################################################################################################

#########################################################################

Result = Redundancy(Infile,IndelType)
Result.LoadGroupfile()
check = True
n=0
while (check == True):
   n=n+1
   positions = Result.Range()
   if (Result.ExtractFragment(positions[0],positions[1]) == False):
      print 'Warning Edge Group: '+str(n)+' - '+str(len(Result.frag))

   Result.RedCandidates()
   Result.AdvanceGroup()
   #checking if Group file Ends
   if positions[2] == True: # The group is the last one
      check = False

#   if(n%500==0):
   print 'Group: '+str(n)+' - '+str(len(Result.frag))
   
# Saving Data and closing Files
Table4file = open(Outfile+'.txt', 'w')     

Table4file.write('Group        ')
Table4file.write('\t')
Table4file.write('rsIDs        ')
Table4file.write('\t')
Table4file.write('Allels       ')
Table4file.write('\t')
Table4file.write('Positions')
Table4file.write('\t')
Table4file.write('Redundancy')
Table4file.write('\n')


count = 0
while count<(len(Result.Table4)):
   string = str( (Result.Table4[count])[0])
   string = string + '\t'+ str( (Result.Table4[count])[1])
   string = string + '\t'+ str( (Result.Table4[count])[2])
   string = string + '\t'+ str( (Result.Table4[count])[3])
   string = string + '\t'+ str( (Result.Table4[count])[4])
   string = string + '\t'+ str( (Result.Table4[count])[5])
   string = string + '\t'+ str( (Result.Table4[count])[6])
   string = string + '\t'+ str( (Result.Table4[count])[7]) + '\n'
   Table4file.write( string )
   count = count + 1 

Table4file.close()

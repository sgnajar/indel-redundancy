#!/usr/bin/pythonw

import sys
import string
from sets import Set
import re


# Files, Input and Output
#Annotation_file  = open('ds_test.flat')
Annotation_file  = open('ds_flat_ch5.flat')
Table1_file      = open('Table1.txt','w')

Annotation_line = ''
Table1_data ="rsID\t"+"type\t"+"Allele\t"+"GRChr37Position\t"+"LocType"+"\n"
Table1_file.write(Table1_data)

NumberofIndels = 0

indelFlag=0
# Parsing the annotiation line by line
for Annotation_line in Annotation_file.readlines():

    #----------------------------------------------------------
    # Parsing Info for rs line
    if re.match('^rs', Annotation_line):
         if 'in-del' in Annotation_line:
           indelFlag=1
           aux = 2

           SeparatorCounter = 0

           # Finding rs_id --> first Separator (|)
           while ( (Annotation_line[aux-1:aux]!='|') and (aux<50+SeparatorCounter*20) ):
               aux=aux+1

           SeparatorCounter = SeparatorCounter + 1
           rs_id = Annotation_line[:aux-1]
           aux = aux + 1

           # Finding Type
           while SeparatorCounter<3:
               while ( (Annotation_line[aux-1:aux]!='|') and (aux<50+SeparatorCounter*20) ):
                   aux=aux+1

               aux = aux + 1
               SeparatorCounter = SeparatorCounter + 1

           SeparatorBegin = aux

           while SeparatorCounter<4:
               while ( (Annotation_line[aux-1:aux]!='|') and (aux<50+SeparatorCounter*20) ):
                   aux=aux+1

               aux = aux + 1
               SeparatorCounter = SeparatorCounter + 1

           mut_type = Annotation_line[SeparatorBegin:aux-2]

        #----------------------------------------------------------
        # End Parsing Info for rs line

    if indelFlag==1:
        #----------------------------------------------------------
        # Parsing Info for Alleles Information line
            if re.match('^SNP', Annotation_line):

               aux = 2

               SeparatorCounter = 0

               # Finding Allel
               while SeparatorCounter<1:
                   while ( (Annotation_line[aux-1:aux]!='|') and (aux<50+SeparatorCounter*20) ):
                       aux=aux+1

                   aux = aux + 1
                   SeparatorCounter = SeparatorCounter + 1

               SeparatorBegin = aux

               while SeparatorCounter<2:
                   while ( (Annotation_line[aux-1:aux]!='|') and (aux<50+SeparatorCounter*20) ):
                       aux=aux+1

                   aux = aux + 1
                   SeparatorCounter = SeparatorCounter + 1

               Alleles = Annotation_line[SeparatorBegin:aux-2]

            #----------------------------------------------------------
            # End Parsing Info for alleles Information line

            #----------------------------------------------------------
            # Parsing Info for Position and Loctype
            if re.match('^CTG', Annotation_line):
                if ('| assembly=GRCh37.p13 |' in Annotation_line):
                   aux = 2

                   SeparatorCounter = 0

                   # Finding Position
                   while SeparatorCounter<3:
                       while ( (Annotation_line[aux-1:aux]!='|') and (aux<50+SeparatorCounter*20) ):
                           aux=aux+1

                       aux = aux + 1
                       SeparatorCounter = SeparatorCounter + 1

                   SeparatorBegin = aux

                   while SeparatorCounter<4:
                       while ( (Annotation_line[aux-1:aux]!='|') and (aux<50+SeparatorCounter*20) ):
                           aux=aux+1

                       aux = aux + 1
                       SeparatorCounter = SeparatorCounter + 1

                   Position = Annotation_line[SeparatorBegin:aux-2]



                   # Finding LocType
                   while SeparatorCounter<7:
                       while ( (Annotation_line[aux-1:aux]!='|') and (aux<50+SeparatorCounter*20) ):
                           aux=aux+1

                       aux = aux + 1
                       SeparatorCounter = SeparatorCounter + 1

                   SeparatorBegin = aux

                   while SeparatorCounter<8:
                       while ( (Annotation_line[aux-1:aux]!='|') and (aux<50+SeparatorCounter*20) ):
                           aux=aux+1

                       aux = aux + 1
                       SeparatorCounter = SeparatorCounter + 1

                   Loctype = Annotation_line[SeparatorBegin:aux-2]

            #----------------------------------------------------------
            # End Parsing Info for Position and Loctype
                NumberofIndels=NumberofIndels+1
                print str(NumberofIndels)+"\n"
                res = rs_id+"\t"+mut_type+"\t"+Alleles+"\t"+Position+"\t"+Loctype+"\n"
                #res = "rsID\t"+"type\t"+"Allele\t"+"GRChr37Position\t"+"LocType"+"\n"
                Table1_file.write(res)
                res = ' '
                indelFlag=0

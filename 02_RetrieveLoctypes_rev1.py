#!/usr/bin/pythonw

import sys
import string
from sets import Set
import re


# Files, Input and Output
Table1_file      = open('Table1.txt','r')
Table2_1file      = open('Table2_1.txt','w')
Table2_3file      = open('Table2_3.txt','w')

Annotation_line = ''
data ="rsID\t"+"Allele\t"+"GRChr37Position\n"
Table2_1file.write(data)
Table2_3file.write(data)


# SeparingLoctypes
for Table1_line in Table1_file.readlines():

    #----------------------------------------------------------
    # Searching for Loctype = 1
    if 'loctype=1' in Table1_line:
        #Remove Type and Loctype
        pos_indel = Table1_line.find("in-del")
        pos_loctype = Table1_line.find("loctype")
        Table2_1line = Table1_line.strip()
        Table2_1line = Table2_1line[:pos_indel]+Table2_1line[pos_indel+7:pos_loctype]


        #removing the word allels and chr-pos
        pos_allele = Table2_1line.find("alleles")
        pos_chr_pos = Table2_1line.find("chr-pos")
        Table2_1line = Table2_1line[:pos_allele]+Table2_1line[pos_allele+8:pos_chr_pos]+Table2_1line[pos_chr_pos+8:]
        Table2_1line=Table2_1line+"\n"

        Table2_1file.write(Table2_1line)

    # Searching for Loctype = 3
    elif 'loctype=3' in Table1_line:
        #Remove Type and Loctype
        pos_indel = Table1_line.find("in-del")
        pos_loctype = Table1_line.find("loctype")
        Table2_3line = Table1_line.strip()
        Table2_3line = Table2_3line[:pos_indel]+Table2_3line[pos_indel+7:pos_loctype]


        #removing the word allels and chr-pos
        pos_allele = Table2_3line.find("alleles")
        pos_chr_pos = Table2_3line.find("chr-pos")
        Table2_3line = Table2_3line[:pos_allele]+Table2_3line[pos_allele+8:pos_chr_pos]+Table2_3line[pos_chr_pos+8:]
        Table2_3line=Table2_3line+"\n"

        Table2_3file.write(Table2_3line)

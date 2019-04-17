#!/bin/bash

echo name : Sasan Najar

chr_Num=5

echo Chromossome $chr_Num



now=$(date +"%r")
echo Step: 0 —> Breaking Reference Sequence in files time : $now
python 00_RefGenBreak_rev1.py refsequence_Chr5_GRCh37p13.fasta 10000
now2=$(date +"%r")
echo Start: $now Finish: $now2

now=$(date +"%r")
echo Step: 1 —> Parse and Retrieve Indel Annotation time : $now
python 01_ParsingAnnotations_rev4_2.py
now2=$(date +"%r")
echo Start: $now Finish: $now2


now=$(date +"%r")
echo Step: 2 —> Retrieve Loctype time : $now
python 02_RetrieveLoctypes_rev1.py
now2=$(date +"%r")
echo Start: $now Finish: $now2

now=$(date +"%r")
echo Step: 3 —> Candidate Groups time : $now
python 03_RedundantIndelGroupCandidates_rev5_9.py Table2_1.txt Table3_1.txt 100
python 03_RedundantIndelGroupCandidates_rev5_9.py Table2_3.txt Table3_3.txt 100
now2=$(date +"%r")
echo Start: $now Finish: $now2

now=$(date +"%r")
echo Step: 4 —> Indel Redundancy Check time : $now
python 04_IndelRedundancyCheck_rev9.py D Table3_1.txt Table4_1_$chr_Num
python 04_IndelRedundancyCheck_rev9.py I Table3_3.txt Table4_3_$chr_Num
now2=$(date +"%r")
echo Start: $now Finish: $now2

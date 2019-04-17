# indel-redundancy

Redundant definition: characterized by similarity or repetition.

A indel is redundant when:
differs only in annotations  (not in the resulting sequences after their modifications to the reference genome).
multiple indels result in the same mutation but are treated as different variants. 

Could be due to: sequencing errors, artifacts caused by ambiguous alignments, and annotation errors

Phases:

1. Data retrieval from NCBI dbSNP – public database for short genetic variants.
Collect the Indel Information by parsing the human genome. 
Indel ID, CHR number, CHR position, allele information and alignment type.

2. Indel alignment type specification verification
To check Indel redundancy   need to determine the alignment type (insertion or deletion) for each indel relative to the reference genome.

3. Candidate redundant indel groups
Based on the retrieved indel position information, the indels are grouped according with their Chr positions, length and type.

4. Indel redundancy check
Pairwise comparison for indel variant substrings generated from indels in the same group;
Human reference genome (GRCh37 build version p10) is downloaded from NCBI

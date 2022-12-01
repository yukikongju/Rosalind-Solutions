## Section 1 - BLAST

We were given this sequence, which was found abundantly in the human patient's
blood sample.

```
>example1
ATGGTGCATCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAG
TTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGG
GGATCTGTCCACTCCTGATGCAGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGT
GCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACT
GTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCA
TCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAAT
GCCCTGGCCCACAAGTATCACTAAGCTCGCTTTCTTGCTGTCCAATTT
```

##### Question 1: Which BLAST program should we use?

There are 3 types of BLAST programs:
    - nucleotide BLAST:
    - protein BLAST:
    - BLASTx: gene finding

Since we are dealing with nucleotides, we will be using BLASTN


##### Question 2: What are the names and accession numbers of the top four hits from your BLAST search?

The top 4 hits are: 
1. [Homo Sapiens Hemoglobin subunit beta](https://www.ncbi.nlm.nih.gov/nucleotide/NM_000518.5?report=genbank&log$=nuclalign&blast_rank=1&RID=SHM60EX5013)
    + Accession: NM_000518
    + Identities: 99%
    + Num Hits: 466/468
2. [Pan Paniscus Hemoglobin subunit beta](https://www.ncbi.nlm.nih.gov/nucleotide/NM_000518.5?report=genbank&log$=nuclalign&blast_rank=1&RID=SHM60EX5013)
    + Accession: XM_003819029
    + Identities: 99%
    + Num Hits: 465/468
3. [Pan troglodytes hemoglobin subunit beta](https://www.ncbi.nlm.nih.gov/nucleotide/XM_508242.4?report=genbank&log$=nuclalign&blast_rank=3&RID=SHM60EX5013)
    + Accession: XM_508242
    + Identities: 99%
    + Num Hits: 465/468
4. [Homo sapiens hemoglobin beta chain variant Hb S-Wake](https://www.ncbi.nlm.nih.gov/nucleotide/AY136510.1?report=genbank&log$=nuclalign&blast_rank=4&RID=SHM60EX5013)
    + Accession: AY136510
    + Identities: 99%
    + Num Hits: 465/468

The accession number is the identifiant of each sequence. It can be found in 
their respective files


##### Question 3: Percent Identities

The percent identifies correspond to the hamming distance between the searched 
sequence (>example1) and the best subsequence hit. They are all at 99%


##### Question 4: How many identical and non identical nucleotides are there in your top hit compared to your last reported hit?

See above


The following questions will be answered using the first hit: Homo Sapiens Hemoglobin subunit beta

##### Question 5: What is the “Official Symbol” and “Official Full Name” for this gene?

- Official symbol: `HBB`
- Official full name: `Homo sapiens hemoglobin subunit beta (HBB), mRNA`

##### Question 6: What chromosome is this gene located on?

The 11th


##### Question 7: What are the names of neighboring genes on this chromosome?



##### Question 8: How many exons and introns are annotated for this gene?




##### Question 9: What is the function of the encoded protein?

reduce protein levels by ~70%

##### Question 10: Does the protein have a role in human disease(s)? If so what diseases?

Sickle Cell Disease

## Section 2 - compare sickle cell and normal β globin sequences to reveal the nature of the sickle cell mutation at the protein level.

[Search Results](https://www.ncbi.nlm.nih.gov/nuccore/?term=HBB)

Entrez keyword: `HBB[Gene Name] AND "Homo sapiens"[Organism]`


##### Q11. What is the ACCESSION number of the “Homo sapiens hemoglobin, beta (HBB), mRNA” entry?

[Source](https://www.ncbi.nlm.nih.gov/nuccore/NM_000518.5)

NM_000518

##### Q12: What are the numbers of the first and last base positions of exon 1 of this entry?

1..142

##### Q13: What are the numbers of the first and last base positions of the CDS?

51..494

Note: CDS stand for 'coding sequence'


## Section 3 - Comparing retrieve sequence with sequence alignment using MUSCLE and SEAVIEW

We input the 2 sequences we want to compare:
```
>example1
ATGGTGCATCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAG
TTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGG
GGATCTGTCCACTCCTGATGCAGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGT
GCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACT
GTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCA
TCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAAT
GCCCTGGCCCACAAGTATCACTAAGCTCGCTTTCTTGCTGTCCAATTT
>NM_000518.5 Homo sapiens hemoglobin subunit beta (HBB), mRNA
ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGA
GGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGC
AGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATG
CTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGC
TCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGAT
CCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCA
CCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCA
CTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACT
GGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGCAA
```

##### Q14: How many gap characters (-) are added to the beginning of the sickle cell beta- globin sequence in order to align it with the beta globin sequence? How might you have guessed this number from information you read in the GenBank annotation?


##### Q15: Ignoring ambiguity codes (Y and N), what are the differences between the two sequences? 



##### Q16: Which codon position from the start of the sickle cell sequence would this
difference affect? What amino acid would the different codons encode in the two
sequences?


## Section 4 -

'''
SPLC exercise 

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. 
        (Note: Only one solution will exist for the dataset provided.)
'''

# dictionary in which each codon correspond to an amino acid 
rna_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'  }

def parser(fasta_data):                
    sequences = []                                                
    seq = ''
    for line in fasta_data.splitlines():
        if line.startswith('>'): 
            if seq:
                sequences.append(seq)
                seq= ''
        else:
            seq += line.strip ()
    if seq:
        sequences.append(seq)
    return sequences

def remove_i(dna_seq, introns):
    for intron in introns:                                # for every intron in introns 
        dna_seq = dna_seq.replace(intron, "")             # remove them from the DNA sequence
    return dna_seq


def rna2protein(rna_seq):
    protein = ""                                          
    for element in range(0, len(rna_seq), 3):             # we read each element in the rna sequnce as groups of 3 (as if they were codons)
        codon = rna_seq[element:element+3]                # we extract said codon
        if codon in rna_table:                            # we check if it is valid 
            aa = rna_table[codon]                         # we get from the rna_table its corresponding amino acid 
            if aa == "Stop":                              # the translation stops at the stop codon
                break  
            protein += aa                                 # we append each amino acid to the empty protein string
    return protein


def dna2protein(fasta_data):
    sequences = parser(fasta_data)                       # we parse the fasta datas
    dna_seq = sequences[0]                               # the frist sequence is the DNA string
    introns = sequences[1:]                              # the remaining sequences are the introns 

    exon_seq = remove_i(dna_seq, introns)                # we remove the introns from the DNA sequence 
    
    rna_sequence = exon_seq.replace("T", "U")            # in the now exons sequence we replace T with U basically transcribing DNA to RNA
    
    protein = rna2protein(rna_sequence)                  # we recall the previuos function to translate RNA into a protein
    return protein

fasta_data = '''>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT'''

print(dna2protein(fasta_data))
'''
mRNA exercise 

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. 
        (Don't neglect the importance of the stop codon in protein translation.)
'''

def mrna(protein):                                   
    codons = {'F': ['UUU', 'UUC'],                                           # dictionary in which every amino amicds is the key to its corresponding codons 
              'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
              'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
              'Y': ['UAU', 'UAC'],
              'Stop': ['UAA', 'UAG', 'UGA'],
              'C': ['UGU', 'UGC'],
              'W': ['UGG'],
              'P': ['CCU', 'CCC', 'CCA', 'CCG'],
              'H': ['CAU', 'CAC'],
              'Q': ['CAA', 'CAG'],
              'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
              'V': ['GUU', 'GUC', 'GUA', 'GUG'],
              'A': ['GCU', 'GCC', 'GCA', 'GCG'],
              'D': ['GAU', 'GAC'],
              'E': ['GAA', 'GAG'],
              'G': ['GGU', 'GGC', 'GGA', 'GGG'],
              'I': ['AUU', 'AUC', 'AUA'],
              'M': ['AUG'],
              'T': ['ACU', 'ACC', 'ACA', 'ACG'],
              'N': ['AAU', 'AAC'],
              'K': ['AAA', 'AAG']}
    number = 1

    for aa in protein:                                                      # for every amino acid in the protein string 
        number = number * len(codons[aa])                                   # calculates the number of codons corresponding to the amino acids 
    number = number*len(codons["Stop"])                                     # we add the stop codons at the end of the string and basically the final result will be multiplied by 3 
    return number % 1000000                                                 # we establish the maximum module limit 

protein = 'MA'
print(mrna(protein))
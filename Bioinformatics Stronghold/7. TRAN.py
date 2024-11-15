'''
TRAN exercise 

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2)
'''

def parser(fasta_data):
    sequences = []
    seq = ""
    for line in fasta_data.splitlines():
        if line.startswith(">"):
            if seq:
                sequences.append(seq)
                seq = ""
        else:
            seq += line.strip()
    if seq:
        sequences.append(seq)
    return sequences

def tt_ratio(s1, s2):
    transitions = 0                                     # we initialize both the trasitions and tranversion counts as 0
    transversions = 0

    # we define the tansitions pairs 
    tt_pairs = {('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')}

    for base1, base2 in zip(s1, s2):                   # we compare 2 sequences base by base 
        if base1 != base2:                             # we only consider the different pairs 
            if (base1, base2) in tt_pairs:             # if the different pairs are a transition
                transitions += 1                       # we increase the transition count 
            else:                                      # if they are not a transition
                transversions += 1                     # we increase the transversion count
    
    return transitions / transversions                 # return the transition and transversion ratio 



fasta_data = '''>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT 
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT'''

sequences = parser(fasta_data)
s1, s2 = sequences[0], sequences[1]
ratio = tt_ratio(s1, s2)
print(ratio)
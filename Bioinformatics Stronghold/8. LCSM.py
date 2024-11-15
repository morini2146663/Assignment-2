'''
LCSM exercise

Given: A collection of k(k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
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

def all_subs(s):
    length = len(s)                                                          # lenght of the string                  
    substrings = []                                       
    for element in range(length):                                            # starting index
        for element2 in range(element + 1, length + 1):                      # ending index
            substrings.append(s[element:element2])                           # we extract the substring from starting to ending index
    return substrings

def l_common_substring(sequences):
    shortest_seq = min(sequences, key=len)                                   # we identify the shortest sequence 
    substrings = sorted(all_subs(shortest_seq), key=len, reverse=True)       # generate shortest sequences and sort them in adescending order
    
    for substr in substrings:                                                # for each substring
        if all(substr in seq for seq in sequences):                          # we check if the said substring exists in all sequences
            return substr                                                    
    return ""                                                                # if no common substring is found an empty string is returned 


fasta_data = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""

print(l_common_substring(parser(fasta_data)))

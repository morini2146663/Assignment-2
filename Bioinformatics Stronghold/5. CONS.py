'''
CONS exercise

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. 
(If several possible consensus strings exist, then you may return any one of them.)
'''

def parser(fasta_data):                                                    
    sequences = {}                                                         
    seq_name = ""
    for line in fasta_data.splitlines():
        if line.startswith(">"):                                           # when a string starts with '>' we idetify her name for the sequences 
            seq_name = line[1:].strip()                                    # we now adds the following rows to the sequences 
            sequences[seq_name] = ""
        else:
            sequences[seq_name] += line.strip()
    return list(sequences.values())                                        # returns a list containing olny the DNA sequneces ignoring the names


def matrix_profile(dna_strings):                                           
    n = len(dna_strings[0])                                                # length of each DNA string, we choose just one string to determine the lenght n
    profile = {'A': [0] * n, 'C': [0] * n, 'G': [0] * n, 'T': [0] * n}     # we create a dictionary with each nucleotide as key 
    
    for dna in dna_strings:                                                # we now fill the profile matrix
        for idx, nucleotide in enumerate(dna):                             # for each DNA sequence we check every nucleotide  
            profile[nucleotide][idx] += 1                                  # and increase the value corrisponding to each nucleotide 
    
    consensus = ""                                                       
    for element in range(n):                                               # for each element of the sequence                                
        max_count = 0                         
        consensus_n = ""
        for nucleotide in "ACGT":                                          # we check profile[nucleotide][element] for every nucleotide
            if profile[nucleotide][element] > max_count:                   # and update both max_count and consensus_nucleotide
                max_count = profile[nucleotide][element]
                consensus_n = nucleotide
        consensus += consensus_n                                           # and we add it to the empty consensus string
    
    return consensus, profile

def print_matrix(profile):                                                
    for nucleotide in "ACGT":
        print(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}")  # print evry nucleotide followed by their corresponding count

fasta_data = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT"""


consensus, profile = matrix_profile(parser(fasta_data))
# consensus -> made by selecting the most recurrent nucleotide in every column
# profile -> matrix containing each nucleotide's count in evry position

print(consensus)
print_matrix(profile)

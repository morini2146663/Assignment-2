'''
REVP exercise

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
'''

def parser(fasta_data):
    sequence = ""
    for line in fasta_data.splitlines():
        if not line.startswith(">"):
            sequence += line.strip()
    return sequence

def reverse(dna):                                                 
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}        # dictionary to use each nucleotide ase key for its complementary
    return "".join(complement[base] for base in reversed(dna))   # we reverse the sequence and repleace each element with its individual

def reverse_palindromes(dna):
    results = []
    n = len(dna)

    for length in range(4, 13):                                  # for every element of legnht between 4 and 13
        for element in range(n - length + 1):                         
            substring = dna[element:element + length]            
            if substring == reverse(substring):                  # if the substring is equal to its reverse complementary string 
                results.append((element + 1, length))            # we append the position and lenght 

    return results

fasta_data = """>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT"""

sequence = parser(fasta_data)
palindromes = reverse_palindromes(sequence)

for position, length in palindromes:
    print(position, length)
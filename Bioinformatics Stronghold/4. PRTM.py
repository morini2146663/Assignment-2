'''
PRTM exercise 

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.
'''

# aa_masses is a dictionary in which every amino acid is the key to its corresponding mass
aa_masses = {
        "A":71.03711, "C":103.00919, "D":115.02694, "E":129.04259, "F":147.06841,
        "G":57.02146, "H":137.05891, "I":113.08406, "K":128.09496, "L":113.08406,
        "M":131.04049, "N":114.04293, "P":97.05276, "Q":128.05858, "R":156.10111,
        "S":87.03203, "T":101.04768, "V":99.06841, "W":186.07931, "Y":163.06333  }

def protein_mass(protein):
    protein_weight = 0                      # we initialize the total protein weight as 0
    for aa in protein:                      # for every amino acid in the protein string 
        protein_weight += aa_masses[aa]     # we get its corresponding weight from the aa_masses table and add it to the total weight 
        
    print(round(protein_weight, 3))         # we round the final result to its 3rd decimal number 

protein = 'SKADYEK'
protein_mass(protein)

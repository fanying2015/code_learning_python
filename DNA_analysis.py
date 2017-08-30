"""In this project, we'll use many of the concepts you've learned throughout the Python course in order to do some DNA analysis for a crime investigation.

The scenario:

A spy deleted important files from a computer. There were a few witnesses at the scene of the crime, but no one is sure who exactly the spy was. Three possible suspects were apprehended based on surveillance video. Each suspect had a sample of DNA taken from them. The computer's keyboard was also swabbed for DNA evidence and, luckily, one small DNA sample was successfully retrieved from the computer's keyboard.

Given the three suspects' DNA and the sample DNA retreived from the keyboard, it's up to you to figure out who the spy is!"""

sample = ['GTA','GGG','CAC']

# Define a method that will take in a file containing DNA sequence, read it, add the file's contents to an empty string, and return the updated string.
def read_dna(dna_file):
  dna_data = ""
  with open(dna_file, "r") as f:
    for line in f:
      dna_data += line
  return dna_data


# a method that will take a string, create a list of codons from that string, and return the list.
def dna_codons(dna):
  codons = []
  for i in range(0, len(dna)):
    if (i+3) < len(dna):
      codons.append(dna[i:(i+3)])
    return codons
  
# a method that automates a task that would normally take a long time to manually complete.
def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches

def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print "The number of matches is %s. Investigation shoud continue" % (num_matches)
  else:
    print "The number of matches is %s. The suspect can be freed" % (num_matches)
    
is_criminal('suspect1.txt')
is_criminal('suspect2.txt')
is_criminal('suspect3.txt')

#!/usr/bin/env python3
#given a sequence and amino acid residue, returns the percent that residue encompasses
def amino_acid_percentages_v1(sequence,residue):
	try:
		return ( sequence.upper().count(residue.upper())/len(sequence) ) * 100
	except(AttributeError, TypeError):
		raise AssertionError('inputs should be strings')

assert round(amino_acid_percentages_v1("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(amino_acid_percentages_v1("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(amino_acid_percentages_v1("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(amino_acid_percentages_v1("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
#given a sequence and a list of residues, will return the total percentage of all given residues
def amino_acid_percentages_v2(sequence, residue=['A','I','L','M','F','W','Y','V']):
	try:
		total = 0
		total = sum((sequence.upper().count(res.upper())/len(sequence))*100 for res in residue)
		return total
	except(AttributeError, TypeError):
		raise AssertionError('inputs should be strings')

assert round(amino_acid_percentages_v2("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(amino_acid_percentages_v2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(amino_acid_percentages_v2("MSRSLLLRFLLFLLLLPPLP")) == 65
#given a dna sequence and a threshold, returns a bool if the count is greater than the threshold
def base_counter(seq, threshold):
	try:
		count = (sum(1 for nuc in seq.upper() if nuc not in "ATCG")/len(seq))*100
		return count >= threshold
	except(AttributeError, TypeError):
		raise AssertionError('Sequence should be string')

assert base_counter("ATCGnnnn",50) == True
assert base_counter("ATCGnnnn",51) == False
assert base_counter("ATGCGTAtttTTGAGCAnnnnnnnnnnn",35) == True
assert base_counter("ATGCGTAtttTTGAGCAnnnnnnnnnnn",50) == False
#given a dna sequence, a kmer size, and a minimum frequency, prints the kmers that occur more often than the minimum frequency
def kmer_counting(dna,kmersize,minfrequency):
	kmers = []
	[kmers.append(dna[idx:idx+kmersize]) for idx in range(len(dna)) if len(dna[idx:idx+kmersize]) == kmersize]	
	uniq_kmers = set(kmers)
	[print(kmer, kmers.count(kmer)) for kmer in uniq_kmers if kmers.count(kmer) >= minfrequency]

#kmer_counting("ATGCATCATG",2,2)	

#takes arguments from kmer_counting and turns them into user inputs and places them in try/catch block
def kmer_user_input():
	try:
		dna = input("Please enter your sequence:")
		kmersize = int(input("Please enter kmer size:"))
		minfrequency = int(input("Please enter how many times you wish the kmer to appear:"))
		kmer_counting(dna,kmersize,minfrequency)
	except(AttributeError,TypeError):
		raise AssertionError('uh oh! There was a type error somewhere. Check to make sure your dna is a string and your other variables are integers')
kmer_user_input()

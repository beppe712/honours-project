import re
import itertools

# Check string file
def check_string(string):
	for char in string:
		if char not in ['A','C','G','T']:
			return False
	return True

# Pattern for generating CBGs
def gen_pattern(pat, g):
	m = len(pat)
	wild = '.'
	cbgs = list()
	wild_indices = itertools.combinations(range(m+g),g)
	for wild_index in wild_indices:
		j = 0 # counter for pattern index
		pattern = ''
		for i in range(m+g):
			if i in wild_index:
				pattern += wild
			else:
				pattern += pat[j]
				j += 1
		cbgs.append(pattern)
	return cbgs

def gen_pattern2(pat, g):
	m = len(pat)
	cbgs = list()
	wild_indices = itertools.combinations(range(m+g),g)
	for wild_index in wild_indices:
		j = 0 # counter for pattern index
		pattern = []
		for i in range(m+g):
			if i not in wild_index:
				pattern += [(i,pat[j])]
				j += 1
		cbgs.append(pattern)
	return cbgs

# Matching
def find_matches(cbgs, string):
	matches = list()
	m_plus_g = len(cbgs[0])
	for i in range(len(string)-m_plus_g+1):
		substring = string[i:i+m_plus_g]
		for cbg in cbgs:
			if re.search(cbg,substring):
				matches.append((i, substring))
				break
	return matches

def find_matches2(cbgs, string, m_plus_g):
	matches = list()
	for i in range(len(string)-m_plus_g+1):
		substring = string[i:i+m_plus_g]
		for cbg in cbgs:
			match = True
			for index, letter in cbg:
				if (substring[index] != letter):
					match = False
					break
			if (match):
				matches.append((i, substring))
				break
	return matches

# Convert string into 0 and 1's
def gen_bin_string(string):
	bin_list = []
	for char in string:
		if char == 'A':
			bin_list += ['00']
		elif char == 'C':
			bin_list += ['01']
		elif char == 'G':
			bin_list += ['10']
		elif char == 'T':
			bin_list += ['11']
	return bin_list

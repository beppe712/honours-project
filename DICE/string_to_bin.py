import sys
from utils import *

def make_bin(stringfpath, outpath, m=0, g=0, r=0):
	stringfile = open(stringfpath, 'r')
	string = stringfile.read()
	stringfile.close()

	string.upper()
	if not check_string(string):
		print('The string contains an invalid character')

	outfile = open(outpath, 'w')
	bin_list = gen_bin_string(string)
	str_len = len(bin_list)

	i = 0

	if (r == 0):
		# for pattern
		for a in range(str_len):
			outfile.write(bin_list[a] + '\n')
		i = str_len

	else:
		# for strings
		for j in range(m+g+r-1):
			if (i < str_len):
				outfile.write(bin_list[i] + '\n')
			else: # Padding
				outfile.write('00\n')
			i += 1
		outfile.write('\n')
		while (i < str_len):
			for j in range(r):
				if (i < str_len):
					outfile.write(bin_list[i] + '\n')
				else: # Padding
					outfile.write('00\n')
				i += 1
			outfile.write('\n')

	outfile.close()

	return i

# Main
def main():
	stringfpath = sys.argv[1]
	outpath = "vivado-project/vivado-project.srcs/sources_1/imports/DICE/string.list"
	m = int(raw_input("Insert length of the pattern: "))
	g = int(raw_input("Insert maximum gap parameter: "))
	r = int(raw_input("Insert number of CLUs: "))
	make_bin(stringfpath,outpath,m,g,r)

if __name__ == "__main__":
    # execute only if run as a script
    main()

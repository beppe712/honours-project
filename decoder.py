import sys
from DICE.utils import *

def decode(string_file, m, g, r, result_file):

	stringfile = open(string_file, 'r')
	string = stringfile.read()
	stringfile.close()

	resultfile = open(result_file, 'r')
	results = resultfile.readlines()
	results = [line.strip() for line in results]

	str_len = len(string)

	for i,line in enumerate(results):
		val = int(line, 16)
		if (val > 0):
			bin_array = [int(bin_val) for bin_val in bin(val)[2:]]
			len_bin_array = len(bin_array)
			for k in range(r-len_bin_array):
				bin_array = [0] + bin_array
			for j,bin_val in enumerate(bin_array):
				if (bin_val == 1):
					if (i*r+j+m+g <= str_len):
						print("({}, '{}')".format(i*r+j,string[i*r+j:i*r+j+m+g]))


def main():
	g = int(raw_input("Insert maximum gap parameter: "))
	r = int(raw_input("Insert number of CLUs: "))
	result_file = sys.argv[1]
	string_file = sys.argv[2]
	pat_path = sys.argv[3]
	patfile = open(pat_path, 'r')
	pat = patfile.read()
	patfile.close()
	m = len(pat)
	decode(string_file, m, g, r, result_file)


if __name__ == "__main__":
    # execute only if run as a script
    main()

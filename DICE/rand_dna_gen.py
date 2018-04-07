import sys
from random import randint

def gen_rand_dna(str_len, file_name):
	outfile = open(file_name,'w')

	alphabet = ['A','C','G','T']
	string = ""

	for i in range(str_len):
		string += alphabet[randint(0,3)]

	outfile.write(string)

	outfile.close()

def main():
	str_len = int(raw_input("Insert string length: "))
	file_name = raw_input("Insert output file name: ")
	gen_rand_dna(str_len, file_name)


if __name__ == "__main__":
    # execute only if run as a script
    main()
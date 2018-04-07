import sys
import time
import datetime
from utils import *

# Print
def print_matches(matches, resultpath):
	if resultpath:
		resultfile = open(resultpath, 'w')
	if not matches:
		print("No matches found")
		return
	for match in matches:
		print(match)
		if resultpath:
			resultfile.write(('{} {}\n'.format(match[0],match[1])))
	if resultpath:
		resultfile.close()
	return

# Main
def main():
	stringfpath = sys.argv[1]
	patfpath = sys.argv[2]
	resultpath = False
	if len(sys.argv) > 3:
		resultpath = sys.argv[3]
	stringfile = open(stringfpath, 'r')
	string = stringfile.read().replace('\n', '')
	stringfile.close()
	patfile = open(patfpath, 'r')
	pat = patfile.read()
	patfile.close()

	string.upper()
	if not check_string(string):
		print('The string contains an invalid character')

	g = int(raw_input("Insert maximum gap parameter: "))
	cbgs = gen_pattern(pat,g)
	start_time = datetime.datetime.now()
	matches = find_matches(cbgs,string)
	print('Elapsed time: {}'.format(datetime.datetime.now() - start_time))
	print_matches(matches,resultpath)
	return

if __name__ == "__main__":
    # execute only if run as a script
    main()

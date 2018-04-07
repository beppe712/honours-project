from string_to_bin import *

def main():
	stringfpath = sys.argv[1]
	outpath = "vivado-project/vivado-project.srcs/sources_1/imports/DICE/pat.txt"
	if len(sys.argv) > 2:
		outpath = sys.argv[2]
	make_bin(stringfpath,outpath)

if __name__ == "__main__":
    # execute only if run as a script
    main()

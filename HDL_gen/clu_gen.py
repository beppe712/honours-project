import sys
from hdl_utils import *
import itertools

def gen_cbg(m,g):
	cbgs = list()
	wild_indices = itertools.combinations(range(m+g),g)
	for wild_index in wild_indices:
		j = 0 # counter for pattern index
		cbg = '('
		for i in range(m+g):
			if i not in wild_index:
				cbg += '(STR[{}] == PAT[{}])'.format(i,j)
				if (j < (m-1)):
					cbg += ' && '
				j += 1
		cbg += ')'
		cbgs.append(cbg)
	return cbgs


def gen_clu(m,g,outpath="clu.sv"):
	outfile = open(outpath,'w')
	outfile.write(gen_heading())
	outfile.write(gen_description("clu","Comparison Logic Unit","None"))

	module_io = """

module clu(
	input 	[1:0] 	STR[0:{}],
	input   [1:0]	PAT[0:{}],
	output			OUT
	);

""".format(m+g-1,m-1)

	outfile.write(module_io)

	module_logic = """

	assign OUT = ("""
	cbgs = gen_cbg(m,g)
	for (i,cbg) in enumerate(cbgs):
		module_logic += cbg
		if (i < (len(cbgs)-1)):
			module_logic += """
		|| """
	module_logic += ");\n\n"

	outfile.write(module_logic)

	outfile.write("endmodule")

	outfile.close()


def main():
	m = int(raw_input("Insert length of the pattern: "))
	g = int(raw_input("Insert maximum gap parameter: "))
	gen_clu(m,g)


if __name__ == "__main__":
    # execute only if run as a script
    main()

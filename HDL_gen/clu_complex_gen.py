from hdl_utils import *

def gen_clu_complex(m,g,r,outpath="clu_complex.sv"):

	outfile = open(outpath,'w+')
	outfile.write(gen_heading())
	outfile.write(gen_description("clu_complex","Comparison Logic Unit","clu"))

	module_io = """

module clu_complex(
	input 	[1:0] 	STR[0:{}],
	input  	[1:0]	PAT[0:{}],
	output	[{}:0]	OUT
	);

""".format(m+g+r-2,m-1,r-1)

	outfile.write(module_io)

	module_logic = """

	genvar cluNo;

	generate
		for (cluNo = 0; cluNo < {}; cluNo = cluNo + 1)
		begin: CLUInstantiation
			clu u_clu (.STR(STR[cluNo:cluNo + {}]), .PAT(PAT), .OUT(OUT[{} - cluNo]));
		end
	endgenerate

""".format(r, m+g-1, r-1)

	outfile.write(module_logic)

	outfile.write("endmodule")

	outfile.close()


def main():
	m = int(raw_input("Insert length of the pattern: "))
	g = int(raw_input("Insert maximum gap parameter: "))
	r = int(raw_input("Insert number of CLUs: "))
	gen_clu_complex(m,g,r)


if __name__ == "__main__":
    # execute only if run as a script
    main()

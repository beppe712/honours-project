from hdl_utils import *

def gen_ssd_wrapper(r,outpath="vivado-project/vivado-project.srcs/sources_1/imports/HDL_gen/ssd_wrapper.sv"):

	outfile = open(outpath,'w+')
	outfile.write(gen_heading())
	outfile.write(gen_description("ssd_wrapper","Two Seven Segment Display Wrapper","ssd_driver"))

	module_io = """

module ssd_wrapper(
	input 			CLK,
	input 			RESET,
	input 			DONE,
	input 	[{}:0]	OUT,
	output 	[6:0]	SSD_A[1:0],
	output			SSD_C
	);

""".format(r-1)

	outfile.write(module_io)

	digits_wrapper_1 = """

	wire [15:0] digits;

	assign digits = {{ {}'d0, OUT }};

""".format(16-r)

	digits_wrapper_2 = """

	wire [15:0] digits;

	assign digits = OUT;

""".format()

	if (r < 16):
		outfile.write(digits_wrapper_1)
	else:
		outfile.write(digits_wrapper_2)

	module_logic_2 = """

	reg [20:0] counter_r;

	initial
		counter_r = 0;

	always @(posedge CLK)
	    counter_r <= counter_r + 1;

	assign SSD_C = counter_r[20];

	genvar ssdNo;

	generate
		for (ssdNo = 0; ssdNo < 2; ssdNo = ssdNo + 1)
		begin: SSDInstantiation
			ssd_driver u_ssd_driver (
				.clk 		(CLK),
				.reset 		(RESET),
				.done 		(DONE),
				.ssd_input 	(digits[(ssdNo * 8)+7 : (ssdNo * 8)]),
				.ssd_c 		(SSD_C),
				.ssd_a 		(SSD_A[ssdNo])
			);
		end
	endgenerate

""".format()

	outfile.write(module_logic_2)

	outfile.write("endmodule")

	outfile.close()


def main():
	r = int(raw_input("Insert number of CLUs: "))
	gen_ssd_wrapper(r)


if __name__ == "__main__":
    # execute only if run as a script
    main()

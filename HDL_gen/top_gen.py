from hdl_utils import *

def gen_top(m,g,r,outpath="top.sv"):

	outfile = open(outpath,'w+')
	outfile.write(gen_heading())
	outfile.write(gen_description("top","Top level module","clu, clu_complex, buffer, ssd_driver, ssd_wrapper"))

	module_io = """

module top(
	input 			CLK,
	input 			RESET,
	input 	[1:0]	BUTTONS,
	output 	[6:0]	SSD_A_0,
	output 	[6:0]	SSD_A_1,
	output	[1:0]	SSD_C,
	output  [1:0]	LEDS
	);

""".format()

	outfile.write(module_io)

	module_logic = """

	wire [1:0] STR[0:{}];
	wire [1:0] PAT[0:{}];
	wire DONE;
	wire [{}:0] OUT;
	wire SSD_C_SINGLE;

    buffer u_buffer(
        .CLK    (CLK),
        .RESET  (RESET),
        .BUTTONS(BUTTONS),
        .STR    (STR),
        .PAT    (PAT),
        .DONE 	(DONE),
  		.LEDS	(LEDS)
    );

	clu_complex u_clu_complex(
        .STR    (STR),
        .PAT    (PAT),
        .OUT 	(OUT)
    );

    ssd_wrapper u_ssd_wrapper(
    	.CLK    (CLK),
        .DONE	(DONE),
        .OUT 	(OUT),
        .SSD_A 	({{SSD_A_1, SSD_A_0}}),
        .SSD_C  (SSD_C_SINGLE)
    );

    assign SSD_C = {{2{{SSD_C_SINGLE}}}};

""".format(m+g+r-2,m-1,r-1)

	outfile.write(module_logic)

	outfile.write("endmodule")

	outfile.close()


def main():
	m = int(raw_input("Insert length of the pattern: "))
	g = int(raw_input("Insert maximum gap parameter: "))
	r = int(raw_input("Insert number of CLUs: "))
	gen_top(m,g,r)


if __name__ == "__main__":
    # execute only if run as a script
    main()

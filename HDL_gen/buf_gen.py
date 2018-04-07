from hdl_utils import *

def gen_buf(m,g,r,str_len,outpath="buffer.sv",sim=False):

	outfile = open(outpath,'w')
	outfile.write(gen_heading())
	outfile.write(gen_description("buffer","String and Pattern buffer","None"))

	module_io = """

module buffer(
	input 				CLK,
	input 				RESET,
	input 		[1:0]	BUTTONS,
	output reg	[1:0] 	STR[0:{}],
	output reg	[1:0]	PAT[0:{}],
	output reg			DONE,
	output		[1:0]   LEDS
	);

""".format(m+g+r-2,m-1)

	outfile.write(module_io)

	count_times = (str_len-(m+g+r-1))/r + 1
	count_size = count_times.bit_length()

	def gen_count_case():
		out = ""
		for i in range(count_times):
			out += """
			{}'d{}: STR <= str_mem[{}:{}];""".format(count_size,i,i*r,i*r+m+g+r-2)
		return out

	module_logic = ""

	if (sim):
		module_logic = """

	reg [1:0] str_mem[0:{}];
	reg [1:0] pat_mem[0:{}];
	reg [{}:0] count;

	initial begin
		$readmemb("pat.list", pat_mem);
		$readmemb("string.list", str_mem);
		count = 0;
		DONE = 0;
	end

	always@(posedge CLK or posedge RESET) begin
		if (RESET) begin
			count <= 0;
			DONE <= 0;
		end
		else if (count >= {})
			DONE <= 1;
		else
			count <= count + 1;
	end

	always@(posedge CLK) begin
		case (count){}
		endcase
		PAT <= pat_mem[0:{}];
	end

	assign LEDS = 2'b00;

""".format(str_len-1,m-1,count_size-1,count_times,gen_count_case(),m-1)

	else:
		module_logic = """

	reg [1:0] str_mem[0:{}];
	reg [1:0] pat_mem[0:{}];
	reg [{}:0] count;

	initial begin
		$readmemb("pat.list", pat_mem);
		$readmemb("string.list", str_mem);
		count = 0;
		DONE = 0;
	end

	always@(posedge CLK or posedge RESET) begin
		if (RESET) begin
			count <= 0;
			DONE <= 0;
		end
		else if (count >= {})
			DONE <= 1;
		else if (((count[0] == 1'b0) && BUTTONS[0]) || ((count[0] == 1'b1) && BUTTONS[1]))
			count <= count + 1;
	end

	always@(posedge CLK) begin
		case (count){}
		endcase
		PAT <= pat_mem[0:{}];
	end

	assign LEDS = (count[0] == 1'b0) ? 2'b01 : 2'b10;

""".format(str_len-1,m-1,count_size-1,count_times,gen_count_case(),m-1)

	outfile.write(module_logic)

	outfile.write("endmodule")

	outfile.close()


def main():
	m = int(raw_input("Insert length of the pattern: "))
	g = int(raw_input("Insert maximum gap parameter: "))
	r = int(raw_input("Insert number of CLUs: "))
	str_len = int(raw_input("Insert length of the string: "))
	sim = False
	if (raw_input("Is this module for simulation? ") in ['yes','y','Yes']):
		sim = True
	gen_buf(m,g,r,str_len,sim=sim)


if __name__ == "__main__":
    # execute only if run as a script
    main()

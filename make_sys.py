from DICE.string_to_bin import make_bin
from HDL_gen.buf_gen import gen_buf
from HDL_gen.clu_complex_gen import gen_clu_complex
from HDL_gen.clu_gen import gen_clu
from HDL_gen.ssd_wrapper_gen import gen_ssd_wrapper
from HDL_gen.top_gen import gen_top

import os
import errno
import sys
from subprocess import call

strings_path = "vivado-project/vivado-project.srcs/sources_1/imports/HDL_gen/"
hdl_path = "vivado-project/vivado-project.srcs/sources_1/imports/HDL_gen/"

for path in [strings_path,hdl_path]:
	if not os.path.exists(path):
		try:
			os.makedirs(path)
		except OSError as exc:
			if exc.errno != errno.EEXIST:
				raise

def make_sys(string_file, pat_file, g, r):

	# Make DNA string binaries
	m = make_bin(pat_file, strings_path + "pat.list")
	str_len = make_bin(string_file, strings_path + "string.list", m, g, r)
	print("Generated string binary files")

	# Make HDL SystemVerilog files
	gen_buf(m,g,r,str_len,hdl_path+"buffer.sv")
	print("Generated buffer HDL")
	gen_clu_complex(m,g,r,hdl_path+"clu_complex.sv")
	print("Generated clu complex HDL")
	gen_clu(m,g,hdl_path+"clu.sv")
	print("Generated clu HDL")
	gen_ssd_wrapper(r,hdl_path+"ssd_wrapper.sv")
	print("Generated SSD wrapper HDL")
	gen_top(m,g,r,hdl_path+"top.sv")
	print("Generated top HDL")

def main():
	string_file = sys.argv[1]
	pat_file = sys.argv[2]
	g = int(raw_input("Insert maximum gap parameter: "))
	r = int(raw_input("Insert number of CLUs: "))
	if (r > 16):
		r = int(raw_input("The physical system supports up to 16 CLUs.\nInsert number of CLUs: "))

	make_sys(string_file, pat_file, g, r)

	if (len(sys.argv) > 3):
		call(['bash','-c',"vivado -nolog -nojournal -mode batch -source setup.tcl"])


if __name__ == "__main__":
    # execute only if run as a script
    main()

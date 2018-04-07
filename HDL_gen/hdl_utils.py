import time
import datetime

# indent_level = 0

def gen_heading():
	return "`timescale 1ns / 1ps\n`default_nettype wire\n"

def gen_description(module="", descr="", depends=""):
	comment_lines = "//////////////////////////////////////////////////////////////////////////////////\n"
	company = "// Company: The University of Edinburgh\n"
	engineer = "// Engineer: Giuseppe Li (s1402587)\n"
	create_date = "// Create Date: {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	design_name = "// Design name: FPGA accelerator for DNA pattern matching\n"
	module_name = "// Module Name: {}\n".format(module)
	project_name = "// Project Name: 4th Year Honours Project (BSc (Hons) Artificial Intelligence and Computer Science)\n"
	description = "// Description: {}\n".format(descr)
	dependences = "// Dependences: {}\n".format(depends)
	additional_comments = "// Additional Comments: This file has been automatically generated\n"
	return (comment_lines +
		company +
		engineer +
		"//\n" +
		create_date +
		design_name +
		module_name +
		project_name +
		description +
		"//\n" +
		dependences +
		"//\n" +
		additional_comments +
		"//\n" +
		comment_lines)




open_project ./vivado-project/vivado-project.xpr -quiet
reset_run synth_1 -quiet
launch_runs impl_1 -to_step write_bitstream -quiet
open_hw -quiet
connect_hw_server -url localhost:3121 -quiet
current_hw_target [get_hw_targets */xilinx_tcf/Digilent/210279655740A]
set_property PARAM.FREQUENCY 15000000 [get_hw_targets */xilinx_tcf/Digilent/210279655740A]
open_hw_target -quiet
wait_on_run impl_1 -quiet
set_property PROGRAM.FILE {./vivado-project/vivado-project.runs/impl_1/top.bit} [lindex [get_hw_devices] 1]
program_hw_devices [lindex [get_hw_devices] 1] -quiet
close_hw
close_project

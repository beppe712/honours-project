`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company:         The University of Edinburgh
// Engineer:        Nigel Topham
//
// Create Date:     17.09.2015 12:36:42
// Design Name:     Practical 2
// Module Name:     ssd_driver
// Project Name:    Computer Design
// Target Devices:  Zync-7010
// Tool Versions:   2015.2
// Description:     Module to drive a seven-segment display from 8-bit integer
//
// Dependencies:    None
//
// Revision:
// Revision 1.0 -   File Created
// Additional Comments:
//
//////////////////////////////////////////////////////////////////////////////////


module ssd_driver(
    input           clk,
    input           reset,
    input           done,
    input  [7:0]    ssd_input,
	input			ssd_c,
    output [6:0]    ssd_a
);

// Define the on/off settings for each segment of a seven-segment digit

localparam BLANK    = 7'h00; //
localparam ZERO     = 7'h3f; // 0
localparam ONE      = 7'h06; // 1
localparam TWO      = 7'h5b; // 2
localparam THREE    = 7'h4f; // 3
localparam FOUR     = 7'h66; // 4
localparam FIVE     = 7'h6d; // 5
localparam SIX      = 7'h7d; // 6
localparam SEVEN    = 7'h07; // 7
localparam EIGHT    = 7'h7f; // 8
localparam NINE     = 7'h6f; // 9
localparam ALFA     = 7'h77; // A
localparam BRAVO    = 7'h7c; // b
localparam CHARLIE  = 7'h39; // C
localparam DELTA    = 7'h5e; // d
localparam ECHO     = 7'h79; // E
localparam FOXTROT  = 7'h71; // F
localparam DASH     = 7'h40; // -t

// Define the decoding from a 4-bit unsigned binary integer to the two
// digits of a seven segment display. This requires 14 bits of output,
// one for each of the seven segments of the two digits. This decoding
// therefore also splits binary numbers into two hexadecimal digits as
// an implicit side effect of the mapping to the SSD.

reg [13:0] ssd_segments;

always @*
begin: ssd_mapping_PROC
  if (done == 1)
    ssd_segments = { DASH, DASH };
  else begin
    case (ssd_input[7:4])
      4'h0:  ssd_segments[13:7] = ZERO;
      4'h1:  ssd_segments[13:7] = ONE;
      4'h2:  ssd_segments[13:7] = TWO;
      4'h3:  ssd_segments[13:7] = THREE;
      4'h4:  ssd_segments[13:7] = FOUR;
      4'h5:  ssd_segments[13:7] = FIVE;
      4'h6:  ssd_segments[13:7] = SIX;
      4'h7:  ssd_segments[13:7] = SEVEN;
      4'h8:  ssd_segments[13:7] = EIGHT;
      4'h9:  ssd_segments[13:7] = NINE;
      4'ha:  ssd_segments[13:7] = ALFA;
      4'hb:  ssd_segments[13:7] = BRAVO;
      4'hc:  ssd_segments[13:7] = CHARLIE;
      4'hd:  ssd_segments[13:7] = DELTA;
      4'he:  ssd_segments[13:7] = ECHO;
      4'hf:  ssd_segments[13:7] = FOXTROT;
    endcase
    case (ssd_input[3:0])
      4'h0:  ssd_segments[6:0] = ZERO;
      4'h1:  ssd_segments[6:0] = ONE;
      4'h2:  ssd_segments[6:0] = TWO;
      4'h3:  ssd_segments[6:0] = THREE;
      4'h4:  ssd_segments[6:0] = FOUR;
      4'h5:  ssd_segments[6:0] = FIVE;
      4'h6:  ssd_segments[6:0] = SIX;
      4'h7:  ssd_segments[6:0] = SEVEN;
      4'h8:  ssd_segments[6:0] = EIGHT;
      4'h9:  ssd_segments[6:0] = NINE;
      4'ha:  ssd_segments[6:0] = ALFA;
      4'hb:  ssd_segments[6:0] = BRAVO;
      4'hc:  ssd_segments[6:0] = CHARLIE;
      4'hd:  ssd_segments[6:0] = DELTA;
      4'he:  ssd_segments[6:0] = ECHO;
      4'hf:  ssd_segments[6:0] = FOXTROT;
    endcase
  end
end // ssd_mapping_PROC

// Time-division multiplex the two digit outputs for the SSD

assign ssd_a = (ssd_c == 1'b1) ? ssd_segments[13:7] : ssd_segments[6:0];

endmodule

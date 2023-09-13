// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/QU02/double/Double.asm

// Doubles R0 and stores the result in R1.
// (R0, R1 refer to RAM[0] and RAM[1] respectively.)

// Set RAM location to 0
@R0
// Assign Data to current RAM location
D=M
// Adds Data + Data
D=D+M

// Set RAM location to 1
@R1
// Store current Data in current RAM location
M=D

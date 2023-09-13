// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/QU02/add/Add.asm

// Adds R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Set RAM location to 0
@R0
// Assign Data to current RAM location
D=M

// Set RAM location to 1
@R1
// Assign Data to Data + current RAM location
D=D+M

// Set RAM location to 2
@R2
// Store current Data in current RAM location
M=D
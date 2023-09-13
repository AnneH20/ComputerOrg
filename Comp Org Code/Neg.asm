// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/QU02/neg/Neg.asm

// Negates R0 and stores the result in R1.
// (R0, R1 refer to RAM[0] and RAM[1] respectively.)

// Set RAM location to 0
@R0
// Assign Data to 
D=-M

// Set RAM location to 1
@R1
// Store current data in current RAM location
M=D
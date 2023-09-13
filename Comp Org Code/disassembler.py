import sys
from os.path import exists as file_exists


### How to run the code ###

# 1. Ensure that Python is setup on your system (Python 3)
#   Run python -V to check

#   python -V Output
#       Python 3.10.4


# 2. Go to the directory where your files are located 
# You can check if your files are there by running 'ls' in the terminal

# 3. Run the following
# python ./disassembler.py "sample.hack"

# You may need to change python to python3 if it fails
# ./ indicates the current directory 
# You will need to substitute "sample.hack" for the appropriate HACK file




# Check if appropriate file extension
if ".hack" in sys.argv[1]:

    # Check if file exists
    if file_exists(sys.argv[1]):

        file = open(sys.argv[1], 'r')
        Lines = file.readlines()

        # List to be used for storing HACK instructions
        hackList = []

        # Computation Dictionary
        compTable = {
            '101010' : '0',
            '111111' : '1',
            '111010' : '-1',
            '001100' : 'D',
            '110000' : 'A,M',
            '001101' : '!D',
            '110001' : '!A,!M',
            '001111' : '-D',
            '110011' : '-A,-M',
            '011111' : 'D+1',
            '110111' : 'A+1,M+1',
            '001110' : 'D-1',
            '110010' : 'A-1,M-1',
            '000010' : 'D+A,D+M',
            '010011' : 'D-A,D-M',
            '000111' : 'A-D,M-D',
            '000000' : 'D&A,D&M',
            '010101' : 'D|A,D|M'
        }

        # Destination Dictionary
        destTable = {
            '000' : '',
            '001' : 'M=',
            '010' : 'D=',
            '011' : 'DM=',
            '100' : 'A=',
            '101' : 'AM=',
            '110' : 'AD=',
            '111' : 'ADM='
        }

        # Jump Dictionary
        jumpTable = {
            '000' : '',
            '001' : ';JGT',
            '010' : ';JEQ',
            '011' : ';JGE',
            '100' : ';JLT',
            '101' : ';JNE',
            '110' : ';JLE',
            '111' : ';JMP'
        }

        # Loop through all assembly lines in the HACK file
        for line in Lines:

            # A Instruction

            # if - Check instruction op-code (the first char in the string)
            if(line[0] == '0'):
                # Get the remaining substring and convert to decimal 
                # Conversion

                value = int(line[1:16], 2)

                # Construct the appropriate HACK instruction
                # https://www.geeksforgeeks.org/python-string-concatenation/

                var1 = '@'
                instruct = var1 + str(value) + '\n'

                # Append to hackList
                # https://www.geeksforgeeks.org/python-list-append-method/
                hackList.append(instruct)



            # C Instruction

            # elif - Check instruction op-code (the first char in the string)
            
            elif(line[0] == '1'):

                # Create strings from the appropriate substrings
                # aBit, cBit, dBit, jBit
                aBit = line[3]
                cBit = line[4:10]
                dBit = line[10:13]
                jBit = line[13:16]

                # Check line 94 
                # or
                # https://www.geeksforgeeks.org/string-slicing-in-python/

                # Return HACK destination string from destTable using dBit
                # https://www.geeksforgeeks.org/python-dictionary/?ref=lbp

                d = destTable[dBit]

                # Return HACK computation string from compTable using cBit 

                c = compTable[cBit]

                # Get the appropriate value by splitting on the comma

                compVal = c.split(',')[int(aBit)]

                # Return HACK jump string from jumpTable using jBit

                j = jumpTable[jBit]

                # Construct the appropriate HACK instruction

                instruct = d + compVal + j + '\n'

                # Append to hackList

                hackList.append(instruct)

        # Write to file
        file = open(sys.argv[1].replace('.hack', '.asm'), 'w')
        file.writelines(hackList)
        file.close()
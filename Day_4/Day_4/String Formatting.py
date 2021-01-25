def print_formatted(number):
    # your code goes here
    Pad= len(str(bin(number))) 
    for i in range(1, number + 1): 
        floatVar = str(i) 
        octVar = str(oct(i)[2:]) 
        hexVar = str(hex(i)[2:]).upper() 
        binVar = str(bin(i)[2:]) 
        formatFloat = ((" " * (Pad - len(str(floatVar)) - 2)) + floatVar) 
        formatOct = ((" " * (Pad - len(str(octVar)) - 2)) + octVar) 
        formatHex = ((" " * (Pad - len(str(hexVar)) - 2)) + hexVar) 
        formatBin = ((" " * (Pad - len(str(binVar)) - 2)) + binVar) 
        print(formatFloat + " " + formatOct + " " + formatHex + " " + formatBin)
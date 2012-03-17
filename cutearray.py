# Parse a text file containing a json print out from a Java toString method to make it pretty

import sys

fileArg = sys.argv[1] 

def cuteArray(filename):
    file = open(filename, 'r')
    t = "   "
    fo = open('cuteArray.txt','w')
    tabs = 0
    balance = 0
    currentbuff=""
    inArray = False
    original = file.readline()
    for char in original:
        if char ==",":
            pass
        elif (not inArray):
            if char=='{':
                tabs+=1
                fo.write(currentbuff+"{\n")
                currentbuff=""
                for x in range(tabs):
                    currentbuff+=t
            elif char=='[':
                tabs+=1
                currentbuff+="[\n"
                fo.write(currentbuff)
                currentbuff=""
                for x in range(tabs):
                    currentbuff+=t
                inArray = True
            elif char=='}':
                tabs-=1;
                if currentbuff.strip():
                    fo.write(currentbuff+"\n")
                bracketbuff=""
                currentbuff=""
                for x in range(tabs):
                    currentbuff+=t
                    bracketbuff+=t
                fo.write(bracketbuff+"}\n")
            else:
                currentbuff+=char
        else:
            if char=="]":
                inArray = False
                tabs-=1
                if currentbuff.strip():
                    fo.write(currentbuff+"\n")
                currentbuff=""
                bracketbuff=""
                for x in range(tabs):
                    currentbuff+=t
                    bracketbuff+=t
                fo.write(bracketbuff+"]\n")
            elif char=="{":
                balance+=1
                currentbuff+="{"
            elif char=="}" and balance == 1:
                balance-=1
                fo.write(currentbuff+"}\n")
                currentbuff=""
                for x in range(tabs):
                    currentbuff+=t
            elif char=="}":
                balance-=1
                currentbuff+=char
            else:
                currentbuff+=char
    file.close()
    fo.close()

cuteArray(fileArg)

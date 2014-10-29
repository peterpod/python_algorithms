def reverseString(string):
    # Reverse the order of the characters
    reverse = ""
    for c in string:
        reverse = c + reverse
    return reverse
 
def colsNeeded(string, rows):
    x = 0
    if (len(string) % rows != 0):
        x = 1 # Forces rounding up without using math.ciel
    return len(string)/rows + x
   
 
def flipOddRows(string, col):
    flipped = ""
    index = 0
    row = 0
    print string
    while index < len(string):
        if row % 2 != 0:
            flipped += reverseString(string[index:index+col])
        else:
            flipped += string[index:index+col]
        index += col
        row += 1
    print flipped
    return flipped
 
def removeLowerCaseAndNumber(encoding):
   text=encoding
   i=0
   while i< len(encoding):   
       if(str.isdigit(encoding[i])):
          text=text[0:i]+text[i+1:len(encoding)] #strips out digits

       elif(ord(encoding[i])<=122 and ord(encoding[i])>=100):
            text=text[0:i]+text[i+1:len(encoding)-1] #strips out lowerase letters
       i+=1
   print text
 
def decodeRightLeftRouteCipher(s):
    encrypted = s[1:]
    rows = int(s[0])
    cols = colsNeeded(s, rows) - 1
    flipped = flipOddRows(encrypted, cols)
    decrypted = ""
    for c in xrange(cols):
        for r in xrange(rows):
            print c*cols + r
            decrypted += flipped[r*cols+c]
    print decrypted
    print removeLowerCaseAndNumber(decrypted)
       
   
decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT")

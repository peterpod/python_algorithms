def  encodeRightLeftRouteCipher(message,numRows):
    encodedS = str(numRows) #adds the number of rows to the encoded string
    i = 0
    numCol = (len(message) + numRows-1) / numRows
    while (len(message) < (numRows * numCol)): #does this to make sure we have a full grid
        message += chr(122-i)
        i = (i + 1) % 26 #goes through alphabet backwards and will loop when it reaches a
    for x in xrange(numRows):
        if (x % 2 == 0):
            for y in xrange(numCol):
                encodedS += message[y*numRows+x]
        if (x % 2 == 1):  # we go backwards on every other row
            for y in xrange(numCol):
                encodedS += message[len(message)-numRows+x-(y*numRows)]
    return encodedS

print encodeRightLeftRouteCipher("WEATTACKATDAWN",4)

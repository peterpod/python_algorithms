def noRepeats(word,letter):
    count=0
    for c in word:
        if(c==letter):
            count+=1
    if(count>1):return False
    return True

print noRepeats("petering","I")

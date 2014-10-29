def flatten(l):
   if type(l) != type([]): return [l]
   if l == []: return l
   else:
      return flatten(l[0]) + flatten(l[1:])
   
assert(flatten([1,[2]]) == [1,2])
print "hi2"
assert(flatten([1,2,[3,[4,5],6],7]) == [1,2,3,4,5,6,7])
print "hi3"
assert(flatten(['wow', [2,[[]]], [True]]) ==['wow', 2, True])
#print "hi4"
assert(flatten([]) ==[])
assert(flatten([[]]) ==[])
assert(flatten(3) == 3)
   

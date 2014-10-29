class A(object):
   def __init__(self, x): self.x = x
   def __str__(self): return "A%d" % self.x
class B(A):
   def __init__(self):
      super(B, self).__init__(5) 
   def __str__(self): return "B%d" % self.x
class C(B):
   def __init__(self, a): self.x = 2*a.x
def p(a):
# Note: each call to p(a) prints 1 line
   print a,
   print type(a).__name__,
   print 1*isinstance(a,A),
   print 1*isinstance(a,B),
   print 1*isinstance(a,C)
p(A(1))
p(B())
p(C(A(3)))

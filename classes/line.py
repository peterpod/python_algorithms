from fractions import Fraction
class Line(object):
    def __init__(self,slope,intercept):
        self.slope=slope
        self.intercept=intercept
    def getSlope(self):
        """Return the slope (m) of the line."""
        return self.slope
    def getIntercept(self):
        return self.intercept
    def getIntersection(self,other):
        pass
    #@classmethod
    def isParallelTo(self,other):
        if(Line.getSlope(self)== Line.getSlope(other)):
           return True
        else:
           return False    
    def __str__(self):
        if(self.slope==0):
           return "y=%s"%(self.intercept)
        elif(abs(self.slope)==1):
           if(self.slope==1):
              if(self.intercept>0):
                 return "y=x+%s"%(self.intercept)
              else:
                 return"y=x%s"%(self.intercept)
           else:
              if(self.intercept>0):
                 return "y=-x+%s"%(self.intercept)
              else:
                 return"y=-x%s"%(self.intercept)       
        elif(self.slope>1):
           if(self.intercept>0):
              return "y=%sx+%s" % (self.slope, self.intercept)
           else:
              return "y=%sx%s" % (self.slope, self.intercept)
        elif(self.slope<0):
           if(self.intercept>0):
              return "y=-%sx+%s" % (self.slope, self.intercept)
           else:
              return "y=-%sx%s" % (self.slope, self.intercept)
        #if slope and  intercept are both a fraction
        elif(int(self.slope)!=self.slope)and(int(self.intercept)!=self.intercept):
           print self.slope>0, self.intercept
           if(self.slope>0):
              if(self.intercept>0):
                 return "y=%s/%sx+%s/%s" % (self.slope.numerator, self.slope.denominator,
                                            self.intercept.numerator,self.intercept.denominator)
              else:
                 return "y=%s/%sx%s/%s" % (self.slope.numerator, self.slope.denominator,
                                            self.intercept.numerator,self.intercept.denominator)
           elif(self.slope<0):
              if(self.intercept>0):
                 return "y=%s/%sx+%s/%s" % (self.slope.numerator, self.slope.denominator,
                                            self.intercept.numerator,self.intercept.denominator)
              else:
                 return "y=%s/%sx%s/%s" % (self.slope.numerator, self.slope.denominator,
                                            self.intercept.numerator,self.intercept.denominator)
        #if slope is only a fraction
        elif(int(self.slope)!=self.slope):
            if(self.slope>0):
              if(self.intercept>0):
                 return "y=%s/%sx+%s" % (self.slope.numerator, self.slope.denominator,
                                            self.intercept)
              else:
                 return "y=%s/%sx%s" % (self.slope.numerator, self.slope.denominator,
                                            self.intercept)
            elif(self.slope<0):
               if(self.intercept>0):
                  return "y=%s/%sx+%s" % (self.slope.numerator, self.slope.denominator,
                                             self.intercept)
               else:
                  return "y=%s/%sx%s" % (self.slope.numerator, self.slope.denominator,
                                             self.intercept)
        #only intercept is fraction
        elif(int(self.intercept)!=self.intercept):
           if(self.slope>0):
              if(self.intercept>0):
                 return "y=%sx+%s/%s" % (self.slope,self.intercept.numerator,self.intercept.denominator)
              else:
                 return "y=%sx%s/%s" % (self.slope,
                                            self.intercept.numerator,self.intercept.denominator)
           elif(self.slope<0):
              if(self.intercept>0):
                 return "y=%sx+%s/%s" % (self.slope,
                                            self.intercept.numerator,self.intercept.denominator)
              else:
                 return "y=%sx%s/%s" % (self.slope,
                                            self.intercept.numerator,self.intercept.denominator)
            
            
    def __repr__(self):
       return "Line(%r, %r)" %(self.slope,self.intercept)
    def __hash__(self):
        return hash((self.slope,self.intercept))
    def __eq__(self, other):
        if(type(self)==type(other)):
           return True
        else:
           return False
        if((Line.getSlope(self)==Line.getSlope(other))and
           (Line.getIntercept(self)==Line.getIntercept(other))):
           return True
        else:
           return False
    def getIntersection(self,other):
        intersectionXNum=(Line.getIntercept(other)-Line.getIntercept(self))
        intersectionXDen=(Line.getSlope(self)-Line.getSlope(other))
        #print intersectionXNum,intersectionXDen
        cx=Fraction(intersectionXNum,intersectionXDen)
        #print cx.numerator, cx.denominator
        y=(Line.getSlope(self)*cx)+Line.getIntercept(self)
        return (cx,y)
    def getNormalLine(self,x):
        self.slope=-1*(1/self.slope)
            
   
           
print "Testing Line class...",

#Line Test 1
assert(str(Line(2,5))  == "y=2x+5")
assert(str(Line(2,-5)) == "y=2x-5")
assert(str(Line(0,5))  == "y=5")
assert(str(Line(1,5))  == "y=x+5")
assert(str(Line(-1,5)) == "y=-x+5")
assert(str(Line(0,-5)) == "y=-5")
assert(str(Line(0,0))  == "y=0")
assert(str(Line(Fraction(2,3),Fraction(1,3)))  == "y=2/3x+1/3")
assert(str(Line(Fraction(2,3),Fraction(-2,6)))  == "y=2/3x-1/3")
print str(Line(Fraction(-2,3),Fraction(2,-6)))
assert(str(Line(Fraction(-2,3),Fraction(2,-6)))  == "y=-2/3x-1/3")
assert(str(Line(Fraction(2,-3),Fraction(2,-6)))  == "y=-2/3x-1/3")
assert(str(Line(Fraction(2,3),4))  == "y=2/3x+4")
assert(str(Line(4,Fraction(2,3)))  == "y=4x+2/3")
#print str([Line(0,1), Line(1,0)])
# hint: be sure to understand the difference between str(x) and repr(x)
assert(str([Line(0,1), Line(1,0)]) == "[Line(0, 1), Line(1, 0)]")
assert(str([Line(Fraction(1,2),3)]) == "[Line(Fraction(1, 2), 3)]")

line1 = Line(2,3)
assert(str(line1) == "y=2x+3")
assert(line1.getSlope() == 2)
assert(type(line1.getSlope()) == int)
assert(line1.getIntercept() == 3)
assert(line1.getSlope.__doc__ == "Return the slope (m) of the line.")


"""
line2 = Line(6,-5)

assert(str(line2) == "y=6x-5")
assert(line2.getSlope() == 6)
assert(line2.getIntercept() == -5)
#Valid up to here
print line1.getIntersection(line2)
assert(line1.getIntersection(line2) == (2, 7))

line3 = Line(2, -3)
assert(line3.isParallelTo(line1) == True)
assert(line3.isParallelTo(line2) == False)

# Two lines intersect in a oint!
#print line3.getIntersection(line2) #(1/2,-2)
print line3.getIntersection(line2)
assert(line3.getIntersection(line2) == (Fraction(1,2), -2))

# The normal line is the line that is perpendicular to
# the given line, intersecting at the given x value.
# Note that the product of the slopes of perpendicular lines is -1.
line4 = line3.getNormalLine(4)
print str(line4)
assert(str(line4) == "y=-1/2x+7")
assert(line4.getSlope() == Fraction(-1,2))
assert(line4.getIntercept() == 7)

assert(Line(1, 2) == Line(1, 2))
assert(Line(1, 2) != Line(1, 3))
print not(Line(1,2))=="dont crash here!"
assert(not(Line(1, 2) == "don't crash here!"))

s = set()
assert(Line(1, 2) not in s)
s.add(Line(1, 2))
assert(Line(1, 2) in s)
s.remove(Line(1, 2))
assert(Line(1, 2) not in s)
"""

print "Passed!"

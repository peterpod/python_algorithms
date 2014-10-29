# hw8.py
# <ppodnies>, <H>

# Implement the required classes (all above the ignore_rest line)
# so that the testAll function runs without errors.
# There are 4 classes to implement: Util, Line, Frog, and RepetitiveFrog.

# Be sure not to modify any code below the ignore_rest line!

# One of the classes models the mathematical notion of a line,
# represented in slope-intercept (m,b) form.  Note that this class
# stores m and b as instances of Python's built-in Fraction class.
# You should read more about that class here:
#     http://docs.python.org/2/library/fractions.html

# One curious thing is that several of our Line class's methods return
# int values for integers but otherwise return Fractions.
# For example, if the slope m is 2, getSlope returns 2, but if the slope is
# 2/3, getslope returns Fraction(2,3).  This is unusual.

from fractions import Fraction

########################
# YOUR CODE GOES HERE! #
########################
class Frog(object):
    message="ribbit!"    
    def speak(self):
        return Frog.message
        
    def __eq__(self):
        pass

    @classmethod
    def setMsg(cls,message):
        Frog.message=message


class RepetitiveFrog(Frog):
    def speak(self):
      return Frog.message+" "+Frog.message+" "+Frog.message

class Util(object):
    def __init__(self,number):
       pass
       
    @classmethod
    def intOrFraction(cls,number):
        if(int(number)==number):
           return int(number)
        else:
           return number

    def __str__(self):
        pass

    def __eq__(self):
        pass

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
           if(self.slope>0):
              if(self.intercept>0):
                 return "y=%s/%sx+%s/%s" % (self.slope.numerator, self.slope.denominator,
                                            self.intercept.numerator,self.intercept.denominator)
              else:
                 return "y=%s/%sx%s/%s" % (self.slope.numerator, self.slope.denominator,
                                            self.intercept.numerator,self.intercept.denominator)
           elif(self.slope<0):
              if(self.intercept>0):
                 return "y=-%s/%sx+%s/%s" % (self.slope.numerator, self.slope.denominator,
                                            self.intercept.numerator,self.intercept.denominator)
              else:
                 return "y=-%s/%sx%s/%s" % (self.slope.numerator, self.slope.denominator,
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
                  return "y=-%s/%sx+%s" % (self.slope.numerator, self.slope.denominator,
                                             self.intercept)
               else:
                  return "y=-%s/%sx%s" % (self.slope.numerator, self.slope.denominator,
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
                 return "y=-%sx+%s/%s" % (self.slope,
                                            self.intercept.numerator,self.intercept.denominator)
              else:
                 return "y=-%sx%s/%s" % (self.slope,
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
   

######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################

def testUtilClass():
    print "Testing Util class...",
    x = Fraction(1,2) # 1/2
    y = Util.intOrFraction(x)
    assert(x is y)

    x = Fraction(2,1)
    y = Util.intOrFraction(x)
    assert((x is not y) and (x == y) and (type(x) == Fraction) and (type(y) == int))
    print "Passed!"

def testLineClass():
    print "Testing Line class...",

    assert(str(Line(2,5))  == "y=2x+5")
    assert(str(Line(2,-5)) == "y=2x-5")
    assert(str(Line(0,5))  == "y=5")
    assert(str(Line(1,5))  == "y=x+5")
    assert(str(Line(-1,5)) == "y=-x+5")
    assert(str(Line(0,-5)) == "y=-5")
    assert(str(Line(0,0))  == "y=0")
    assert(str(Line(Fraction(2,3),Fraction(1,3)))  == "y=2/3x+1/3")
    assert(str(Line(Fraction(2,3),Fraction(-2,6)))  == "y=2/3x-1/3")
    # hint: be sure to understand the difference between str(x) and repr(x)
    assert(str([Line(0,1), Line(1,0)]) == "[Line(0, 1), Line(1, 0)]")
    assert(str([Line(Fraction(1,2),3)]) == "[Line(Fraction(1, 2), 3)]")
    
    line1 = Line(2,3)
    assert(str(line1) == "y=2x+3")
    assert(line1.getSlope() == 2)
    assert(type(line1.getSlope()) == int)
    assert(line1.getIntercept() == 3)
    assert(line1.getSlope.__doc__ == "Return the slope (m) of the line.")

    line2 = Line(6,-5)
    assert(str(line2) == "y=6x-5")
    assert(line2.getSlope() == 6)
    assert(line2.getIntercept() == -5)

    assert(line1.getIntersection(line2) == (2, 7))
    
    line3 = Line(2, -3)
    assert(line3.isParallelTo(line1) == True)
    assert(line3.isParallelTo(line2) == False)

    # Two lines intersect in a point!
    assert(line3.getIntersection(line2) == (Fraction(1,2), -2))

    # The normal line is the line that is perpendicular to
    # the given line, intersecting at the given x value.
    # Note that the product of the slopes of perpendicular lines is -1.
    line4 = line3.getNormalLine(4)
    assert(str(line4) == "y=-1/2x+7")
    assert(line4.getSlope() == Fraction(-1,2))
    assert(line4.getIntercept() == 7)
    
    assert(Line(1, 2) == Line(1, 2))
    assert(Line(1, 2) != Line(1, 3))
    assert(not (Line(1, 2) == "don't crash here!"))

    s = set()
    assert(Line(1, 2) not in s)
    s.add(Line(1, 2))
    assert(Line(1, 2) in s)
    s.remove(Line(1, 2))
    assert(Line(1, 2) not in s)

    print "Passed!"



def testFrogClass():
    print "Testing Frog class...",
    frog1 = Frog()
    assert(frog1.speak() == "ribbit!")
    frog2 = RepetitiveFrog()
    assert(isinstance(frog2, Frog) == True)
    assert(type(frog2) == RepetitiveFrog)
    assert(frog2.speak() == "ribbit! ribbit! ribbit!")
    
    Frog.setMsg("oink?")
    assert(frog1.speak() == "oink?")
    assert(frog2.speak() == "oink? oink? oink?")

    print "Passed!"

def testAll():
    testUtilClass()
    testLineClass()
    testFrogClass()

testAll()

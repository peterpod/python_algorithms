def maximum():
   for x in range(100):
      for y in range(100):
         if((x|y) >= max(x,y))==False:
            print x,y, (x|y), max(x,y)
            return False
   return True

print maximum()

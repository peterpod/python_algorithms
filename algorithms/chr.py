def character():
   for n in range(0,256):
      if(ord(chr(n))!=n):
         return False
   return True

print character()

def hasBalancedParentheses(s):
   # this version has a bug!
   p = 0
   for c in s:
       if (c == "("): p += 1
       elif (c == ")"): p -= 1
       if (p > 0): return False
   return True

print hasBalancedParentheses("))((")

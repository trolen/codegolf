def b(n): return (str(n) if n>0 else "no")+" bottle"+("s" if n!=1 else "")+" of beer"
def w(n): return b(n)+" on the wall"
for i in range(99,0,-1): print "\n"+w(i)+", "+b(i)+"\nTake one down, pass it around, "+w(i-1)

import numpy as np
import sys
d=[list('ABCDEFTUVWXGS567YHR498ZIQ3210JPONMLK')[6*i:6*(i+1)] for i in range(6)]
n=sys.argv[1]
if n in "234": d=np.rot90(d,-1 if n=="2" else 2 if n=="3" else 1)
print '\n'.join(' '.join(c for c in r) for r in d)

def mToNonoM(M):
	mOut = []
	for m in M:
		mOut.append(m)
		mOut.append([])
	return mOut

def createMatrixP(h,w):
	matrix = []
	for lin in range(0,h):
		l = []		
		for col in range(0,w):
			l.append([])
		matrix.append(l)
	return matrix

def g1X(n, nv):
  return gt((n-nv))

def g1YZ(n):
  return gt((n-1))

def g2XY(n, nv):
  return gt((n-nv+1))

def g2Z(n, nv):
  return gt((n-nv))

def gt(t):
  T = []
  for number in range(0,t):
    T.append(1)
  return T

def countElements(M):
  N = {}  #Dict
  for triple in M:
    for element in triple:
      if element in N: #O(1) hash
        N[element] += 1
      else:
        N[element] = 1
  return N

def consColDefinition(M,X,Y,Z,n):
  C = []
  N = countElements(M)
  C.append(gt(n))
  for x in X:
    nv = N[x]
    xi = g1X(n, nv)
    xii = g2XY(n, nv)
    C.append(xi)
    C.append(xii)
  for y in Y:
    nv = N[y]
    yi = g1YZ(n)
    yii = g2XY(n, nv)
    C.append(yi)
    C.append(yii)
  for z in Z:
    nv = N[z]
    zi = g1YZ(n)
    zii = g2Z(n, nv)
    C.append(zi)
    C.append(zii)
  C.append(gt(n))
  return C

def f1(i):
  return (2*i-1)

def f2(q,j,i):
  return (2*(q+j-i)-1)

def f3(q,k,j):
  return (2*(q+k-j)-1)

def f4(q,k):
  return (2*(q-k)+1)

def consRowDefinition(M,X,Y,Z,q):
  R = []
  for triple in M:
    xi = X[triple[0]]
    yj = Y[triple[1]]
    zk = Z[triple[2]]
    ri = []
    r1 = f1(xi)
    r2 = f2(q,yj,xi) 
    r3 = f3(q,zk,yj)
    r4 = f4(q,zk)
    ri = [r1,r2,r3,r4]
    rii = [0]
    R.append(ri)
    R.append(rii)
  return R

def reduction(ThreeDM):
  M = ThreeDM['M']
  X = ThreeDM['X']
  Y = ThreeDM['Y']
  Z = ThreeDM['Z']
  q = ThreeDM['q']
  n = len(M);
  h = 2*n;
  w = 6*q+2;
  R = consRowDefinition(M,X,Y,Z,q);
  C = consColDefinition(M,X,Y,Z,n);
  Nonogram = {'h':h,'w':w,'R':R,'C':C}
  return Nonogram


ThreeDM = {'M' : [['x1','y1','z1'],['x1','y2','z3'],['x2','y2','z3'],['x2','y3','z2'],['x3','y2','z3'],['x3','y3','z2']],
       'X' : {'x1':1,'x2':2,'x3':3},
       'Y' : {'y1':1,'y2':2,'y3':3},
       'Z' : {'z1':1,'z2':2,'z3':3},
       'q' : 3}




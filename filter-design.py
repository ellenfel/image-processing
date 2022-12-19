#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#impors libs
import numpy 
from PIL import Image

I = Image.open("cameraman-og.png").convert("L")
I.show()
    
Inoisy = Image.open("salty-cameraman.jpg").convert("L")
Inoisy.show()

Inoisy_arr = numpy.array(Inoisy)
h=len(Inoisy_arr)
w=len(Inoisy_arr[0])
B = numpy.ones((h,w))
S = numpy.zeros((h,w))

#proposed filter application
#Step 2: determining the noisy pixels in the matrix

for i in range(h):
    for j in range(w):
        if(Inoisy_arr[i,j] == 0 or Inoisy_arr[i,j] == 255):
            B[i,j] = Inoisy_arr[i,j];
        
#Step 3: Set the binary mask(to detect the position)
for i in range(h):
    for j in range(w):
        if(B[i,j] != 1):
            S[i,j] = 1
        else:
            S[i,j] = 0

#step 4:        
Inoisy_before = Inoisy

k = 3;
fkh = k//2
fkw = k//2

U = numpy.pad(Inoisy_arr, (1, 1))
Y = numpy.pad(S, (1, 1))
m= 0
n= 0

i=fkh
j=fkw
c=1
e=1

for r in range(3):
    for i in range(h-fkh):
        for j in range(w-fkw):
            if(Y[i,j] != 0 and k==3):
                V = uceuc(U,i,j)
                Z = uceuc(Y,i,j)
                for c in range(3):
                    for e in range(3):
                        if(c == 2 and e ==2):
                            continue
                        else:
                            q=V[c,e] * Z[c,e] * (1/(abs(c-2) + abs(e - 2)))
                            s=Z[c,e] * (1/(abs(c-2) + abs(e - 2)))
                            m=q + m
                            n=s + n
                p = m / n
                U[i,j] = p
                        

        
        
        
        
        
def uceuc(b,x,y):
    v = numpy.zeros((3, 3), dtype=float)
    v[1,1] = b[x-1,y-1]
    v[1,2] = b[x,y-1]
    v[1,3] = b[x+1,y-1]

    v[2,1] = b[x-1,y]
    v[2,2] = b[x,y]
    v[2,3] = b[x+1,y]

    v[3,1] = b[x-1,y+1]
    v[3,2] = b[x,y+1]
    v[3,3] = b[x+1,y+1]

    return v
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        



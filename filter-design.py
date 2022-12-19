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
#Step 1: determining the noisy pixels in the matrix

for i in range(h):
    for j in range(w):
        if(Inoisy_arr[i,j] == 0 or Inoisy_arr[i,j] == 255):
            B[i,j] = Inoisy_arr[i,j];
        
#Step 2: Set the binary mask(to detect the position)
for i in range(h):
    for j in range(w):
        if(B[i,j] != 1):
            S[i,j] = 1
        else:
            S[i,j] = 0
        
Inoisy_before = Inoisy

k = 3;
fkh = k//2
fkw = k//2

U = numpy.pad(Inoisy_arr, (1, 1))
Y = numpy.pad(S, (1, 1))
m= 0
n= 0



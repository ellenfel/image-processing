from filters import filters
from headers import importAll

import numpy
from PIL import Image
importAll()


# original image with noise
img0 = Image.open("salty-cameraman.jpg").convert("L")
arr = numpy.array(img0)
img0.show()

# performing filters
removed_noise_pd = filters.purposed_design(arr, 3) 
removed_noise_mf = filters.median_filter(arr, 3) 

# results
img1 = Image.fromarray(removed_noise_pd)
img1.show()
img2 = Image.fromarray(removed_noise_mf)
img2.show()

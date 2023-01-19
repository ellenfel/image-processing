import numpy
from PIL import Image


def median_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = []
    data_final = numpy.zeros((len(data),len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final

def main():
    img = Image.open("salty-cameraman.jpg").convert("L")
    arr = numpy.array(img)
    removed_noise = median_filter(arr, 3) 
    img = Image.fromarray(removed_noise)
    img.show()

main()



"""
1. allocate outputPixelValue[image width][image height]
2. allocate window[window width × window height]
3. edgex := (window width / 2) rounded down
4. edgey := (window height / 2) rounded down
    

    for x from edgex to image width - edgex do
    for y from edgey to image height - edgey do
        i = 0
        for fx from 0 to window width do
            for fy from 0 to window height do
                window[i] :=
                inputPixelValue[x + fx - edgex][y + fy - edgey]
                i := i + 1
        sort entries in window[]
        outputPixelValue[x][y] :=
        window[window width * window height / 2]    
"""























                     
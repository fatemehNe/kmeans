import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
import random
import copy
  
# Read Images 
img = mpimg.imread('imageLarge.png') 
mpimg.imsave('imageLarge.png',img)
 
newimg = []

#img[i][j] = newimg[800*i+j]
for i in range(img.shape[0]) :
    for j in range(img.shape[0]) :
        newimg.append(img[i][j])


#kmeans
k = 16
length = len(newimg)

# find initial centroids
centroid =[]
for i in range(0,k):
   centroid.append(newimg[random.randint(0,length+1)])


clstr = []

previousclstr = []
#initialize previousclstr
for i in range(0,length) :
  newimg[i][3] = i % k
for i in range(0,k) : 
    temp = []
    for j in range(0,length):
        if newimg[j][3] == i :
            temp.append(newimg[j])
    previousclstr.append(temp)

########### where loop begins
# assign clusters
strt = False
cnt = 0
while (cnt < k) :
    cnt = 0
    for i in range(0,length):
      min = 20
      for j in range(0,k) : 
         p = newimg[i]
        
         dist = (centroid[j][0] - p[0])**2 + (centroid[j][1] - p[1])**2 + (centroid[j][2] - p[2])**2 
         if min > dist :
               min = dist
               newimg[i][3] = j


   #seperate clusters for checking changes
    if strt == True :
        previousclstr =copy.deepcopy(clstr)
    for i in range(0,k) : 
        temp = []
        for j in range(0,length):
            if newimg[j][3] == i :
                temp.append(newimg[j])
        clstr.append(temp)

    for i in range(0,k) : 
        b = 0
        if len(previousclstr[i]) == len(clstr[i]):
            l =  len(previousclstr[i])
        else :
            b = 0
            cnt = 16
            break
        for j in range(0,l) :
            for m in range(0,3):
                if previousclstr[i][j][m] ==  clstr[i][j][m] :
                    b =  1
                else :
                    b = 0
        if b == 0 :
            cnt = 16
        

    #find new centroids
    for i in range(0,k) : 
        centroid[i] = [ clstr[i][0].mean() , clstr[i][1].mean()  , clstr[i][2].mean()]
    strt = True

#change values
for j in range(0,length) :        
    for i in range(0,k) : 
        if newimg[j][3] == k :
            for  m in range(0,3):
                newimg[j][m] = centroid[k][m]        

#img[i][j] = newimg[800*i+j]
for i in range(0,length) :
    x = int(i / img.shape[0])
    y = int (i % img.shape[0])
    img[x][y]= newimg[i]

# Output Images 
plt.imshow(img)
plt.show()


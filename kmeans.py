import pandas
import random
from matplotlib import pyplot
import copy

dt = pandas.read_csv('dataset2.csv')

k = 2 #num of clusters
dt["L"] = k

length = dt.shape[0]
# find initial centroids
centroid =[]
for i in range(0,k):
   centroid.append([dt.ix[random.randint(0,length+1)]["X"] , dt.ix[random.randint(0,length+1)]["Y"]])


clstr = []
previousclstr = []
#initialize previousclstr
for i in range(0,length) :
  dt.L.iloc[i] = i % k
for i in range(0,k) : 
    previousclstr.append( dt.loc[dt["L"] == i])

########### where loop begins
# assign clusters
strt = False
cnt = 0
while (cnt < k) :
   cnt = 0
   for i in range(0,length):
      min = 20
      for j in range(0,k) : 
         x = dt.ix[i]["X"]
         y = dt.ix[i]["Y"]
         dist = (centroid[j][0] - x)**2 + (centroid[j][1] - y)**2 
         if min > dist :
               min = dist
               dt.L.iloc[i] = j

   #seperate clusters for checking changes
   if strt == True :
      previousclstr =copy.deepcopy(clstr)
   for i in range(0,k) : 
      clstr.append( dt.loc[dt["L"] == i])

   for i in range(0,k) : 
      if previousclstr[i].equals(clstr[i]) :
         cnt +=1

   #find new centroids
   for i in range(0,k) : 
      centroid[i] = [ clstr[i]["X"].mean() , clstr[i]["Y"].mean()]
   strt = True

x=[]
y=[]
for i in range(0,k) :
   x.append(clstr[i]["X"])
   y.append(clstr[i]["Y"])

#error calculation
# dst=[]
# for j in range(0,k) : 
#    dst.append(0)
# for j in range(0,k) : 
#    cj =  clstr[j]
#    for i in range (0 , len(clstr[j])) :
#       x = cj.loc[i]["X"]  
#       y = cj.loc[i]["Y"]
#       dst[j] += (centroid[j][0] - x)**2 + (centroid[j][1] - y)**2 
#    dst[j]= dst[j]/len(clstr[j]+1)

# avger = sum(dst)/k
# print("--------------------",avger)

pyplot.plot(x[0] , y[0],'bo' , label="C0" , color = "red" )
pyplot.plot(x[1] , y[1],'bo' , label="C1" , color = "blue" )
# pyplot.plot(x[2] , y[2],'bo' , label="C2" , color = "orange" )
# pyplot.plot(x[3] , y[3],'bo' , label="C3" , color = "yellow" )


pyplot.show()
   
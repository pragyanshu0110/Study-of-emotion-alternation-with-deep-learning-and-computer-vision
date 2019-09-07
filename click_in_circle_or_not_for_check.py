import numpy as np
import math
from numpy import loadtxt

a = loadtxt("mouse_log_for_check.txt",comments="#",delimiter=",",unpack=False)

n=a.shape[0]
list_of_centers=[(76,83),(1002,78),(1839,84),(75,517),(1023,550),(1848,562),(82,999),(1014,1000),(1833,1006)]

def distance_bw_pts(x1,y1,x2,y2):
	flag=0
	dis=int(math.sqrt((x1-x2)**2+(y1-y2)**2))
	#print(dis)
	if dis <= 60:
		flag=1
	return flag	
	

list_of_prev_cent=[]
count=0
for i in range(0,n):
	if a[i][2]==2:
		x=a[i][0]
		y=a[i][1]
		for j in range(9):
			if (list_of_centers[j][0],list_of_centers[j][1]) not in list_of_prev_cent:
				f = distance_bw_pts(x,y,list_of_centers[j][0],list_of_centers[j][1])
				if f==1:
					count=count+1
					list_of_prev_cent.append((list_of_centers[j][0],list_of_centers[j][1]))


		
print(count)
#if count==9:
#	print("the clicks are CORRECT")
#if count!=9:
#	print("the clicks are INCORRECT")


				








 
 
   
''' this file consist of "prefinal.py + checking"  '''

import os
import time
import pandas as pd

no_clicks=0
percent=0

while (no_clicks!=9) or (percent<90):
	os.remove('check_out.csv')
	os.system("python3 final_for_check.py")
	df=pd.read_csv('check_out.csv', sep=',',header=None)
	no_clicks=df[0][0]
	#print(n)
	if(os.stat("emotion_percent_for_check.csv").st_size==0):
		percent=0
	if(os.stat("emotion_percent_for_check.csv").st_size!=0):	
		df2=pd.read_csv('emotion_percent_for_check.csv', sep=',',header=None)
		percent=int(df2[-1:][0])
	print("percent=",percent)	
os.system("python3 prefinal.py")
import pandas as pd 
import matplotlib.pyplot as plt
import joblib
import numpy as np
import os

def isnumberr(numb):
	#print(num)
	num = str(numb)
	#print("*")
	isdec=0
	#isneg=0
	r=0
	if(num[0]=='-'):
		r=1
			
	for i in range(r,len(num)):
		if(num[i]>'9' or num[i]<'0'):
			if(num[i]=='.' and isdec==0):
				isdec=1
			else:
				return False
	
	return True
		
pathgiven=input("Enter the path of file:")
y = int(input("Enter the year: "))
print("Following are measures for yaxis to plot graph(xaxis:Months):")
print("1-Wind Direction")
print("2-Wind speed")
print("3-Temperature")
print("4-Pressure")
print("5-Humidity")
print("6-Dew point")
option = int(input("Choose One of the above:"))
#fol = "csv/"
fol = pathgiven+"/"

answer=[]
months=[]

#query
query={"1":"Wind Direction"
	,"2":"Wind speed",
	"3":"Temperature",
	"4":"Pressure",
	"5":"Humidity",
	"6":"Dew point"
	}

#csvNotations
csvNot={"1":"2","2":"3","3":"4","4":"6","6":"5"} 

#xlsxNotations
xlsxNot={"1":"3","2":"4","3":"5","4":"6","5":"7","6":"8"} 

#MonthNames
monName={"1":"Jan","2":"Feb","3":"Mar","4":"Apr","5":"May","6":"Jun","7":"Jul","8":"Aug","9":"Sep","10":"Oct","11":"Nov","12":"Dec"}

#csv/i
for i in range (y,y+1):

	
	#csv/i/j
	for j in range (1,13):
	
		if(os.path.isdir(fol+str(i)+"/"+str(j))==True):
			months.append(j)
			
			Mans=0
			Mnum=0
			directory = os.fsencode(fol+str(i)+"/"+str(j))
			
			for file in os.listdir(directory):
				fname = os.fsdecode(file)
				##if file is csv
				if(fname[-3:]=="csv"):

					print(fol + str(i) + "/" + str(j) + "/" + fname)
					# .csv
					dataframe = pd.read_csv(fol + str(i) + "/" + str(j) + "/" + fname)
					newname = []
					total_cols = len(dataframe.axes[1])
					for coll in range(0, total_cols):
						newname.append(str(coll))

					dataframe.columns = newname
					myfilename = "" + fol + str(i) + "/" + str(j) + "/" + fname + ""
					newOpt = csvNot[str(option)]
					col = dataframe[str(newOpt)]
					mean = 0
					num = 0
					flag = 0
					for k in range(0, len(col)):
						if (isnumberr(col[k]) == True):
							flag = 1
							mean += (float(col[k]))
							num += 1
					if (flag == 1):
						ans = mean / num  ##1 day
						Mnum += 1 ##no of days
						Mans += ans
				if (fname[-4:] == "xlsx"):

					if(isnumberr(fname[:2])==True):

						myfilename = ""+fol+str(i)+"/"+str(j)+"/"+fname+""
						print(fol+str(i)+"/"+str(j)+"/"+fname)
						#.xlsx
						dataframe = pd.read_excel(myfilename,"Sheet1")
						mean=0
						num=0
						flag=0

						total_rows=len(dataframe.axes[0])
						total_cols=len(dataframe.axes[1])

						newOpt = xlsxNot[str(option)]
						newOpt = int(newOpt)
						for k in range(4,total_rows):
							if(isnumberr(dataframe.iloc[k][newOpt])==True):
								flag=1
								mean+=(float(dataframe.iloc[k][newOpt]))
								num+=1
						if(flag==1):
							ans=mean/num
							Mnum+=1
							Mans+=ans
			finalAns=Mans/Mnum		#Mean of every month
			answer.append(finalAns)		

plt.plot(months,answer,marker='o', markerfacecolor='red', markersize=9)
plt.xlabel('Month') 
# naming the y axis 
plt.ylabel(query[str(option)]) 
plt.show()
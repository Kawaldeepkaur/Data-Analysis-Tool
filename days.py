import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
import os


#HANDLES NULL OR NOT AVAILABLE VALUES
def isnumberr(numb):
	num = str(numb)
	isdec=0
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
	
#csv/2015/1
path = input("Enter Month File Path : ")
print("Following are measures for yaxis to plot graph(xaxis:Months):")
print("1-Wind Direction")
print("2-Wind speed")
print("3-Temperature")
print("4-Pressure")
print("5-Humidity")
print("6-Dew point")
option = int(input("Choose One of the above:"))
path=path+"/"
DayAns=[]
Dayno=[]
directory = os.fsencode(path+"/")
dayNo=0
for file in os.listdir(directory):
	dayNo+=1;
	fname=os.fsdecode(file)
	##FILE EXTENSION --> .csv
	if(fname[-3:]=="csv"):
		dataframe = pd.read_csv(path+fname)
		newname=[]
		total_cols=len(dataframe.axes[1])
		for coll in range(0, total_cols):
			newname.append(str(coll))

		dataframe.columns = newname
		
		newOpt = csvNot[str(option)]
		col = dataframe[str(newOpt)]
		mean = 0
		num = 0
		flag = 0
		for k in range(0, len(col)):
			if (isnumberr(col[k]) == True):
				# print
				flag = 1
				mean += (float(col[k]))
				num += 1
		if (flag == 1):
			ans = mean / num  ##1 day
			DayAns.append(ans)
			Dayno.append(dayNo)
	
	##FILE EXTENSION --> .xlsx	
	if (fname[-4:] == "xlsx"):
		if(isnumberr(fname[:2])==True):

			myfilename = ""+path+fname+""
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
				DayAns.append(ans)
				Dayno.append(dayNo)
	
plt.plot(Dayno,DayAns,marker='o', markerfacecolor='red', markersize=9)	


plt.xlabel('Day') 
# naming the y axis 
plt.ylabel(query[str(option)]) 
plt.show()	
	
from datetime import date, datetime
# time_now=datetime.now()
# time_now=datetime(2022, 3, 18, 17, 25, 30)
# a = datetime(2022, 3, 19, 18, 25, 30)
# d_a=a.strftime('%d/%m/%Y')


# # Function to convert string to datetime
# def convert(date_time):

# 	datetime_str = datetime.strptime(n[2]+" "+n[1], '%d/%m/%Y %H:%M:%S')

# 	return datetime_str

# # Driver code
# n=["ASHISH_PATIL","18:14:22","15/03/2022"]
# print(convert(n))


# tStr=time_now.strftime('%H:%M:%S')
# dStr=time_now.strftime('%d/%m/%Y')

# c=a-time_now
# c_in_s=c.total_seconds()
# days  = c.days                         # Build-in datetime function

# print(a)
# days    = divmod(c_in_s, 86400)        # Get days (without [0]!)
# hours   = divmod(days[1], 3600)               # Use remainder of days to calc hours
# minutes = divmod(hours[1], 60)                # Use remainder of hours to calc minutes
# seconds = divmod(minutes[1], 1)               # Use remainder of minutes to calc seconds
# print("Time between dates: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0]))
   # hog transformation encoding used
def attendance(name):
        print(name)
        with open('Attendance.csv','r+') as f:
            myDataList=f.readlines()
            nameList=[]
            entryList=[]

            for line in myDataList:
                entry=line.split(',')
                
                entryList.append(entry)
                nameList.append(entry[0])
            print(entryList)
            if name not in nameList:
                time_now=datetime.now()
                tStr=time_now.strftime('%H:%M:%S')
                dStr=time_now.strftime('%d/%m/%Y')
             
                f.writelines(f'{name},{tStr},{dStr}')
            i=0
            print(nameList)
            for n in nameList:
              
                if(name==n):
               
                    time_now=datetime.now()
                    print(entryList[i])
                    # time_now=datetime.now()
                    # prev=datetime.strptime(entryList[i][2]+" "+entryList[i][1],'%d/%m/%Y %H:%M:%S')
                    # time_diff=time_now-prev
                    # print(time_diff.days)
                    time_diff= datetime.now() - datetime.strptime(entryList[i][2]+" "+entryList[i][1],'%d/%m/%Y %H:%M:%S' )
                    duration=time_diff.total_seconds()
                    days    = divmod(duration, 86400)        # Get days (without [0]!)
                    hours   = divmod(days[1], 3600) 
                    # print(type(int(hours[0])))   
                    # # print("days=",time_diff.days)
                    
                    print(days)
                    if( int(days[0])>=1):
                         time_now=datetime.now()
                         tStr=time_now.strftime('%H:%M:%S')
                         dStr=time_now.strftime('%d/%m/%Y')
                         print("hoo")
                         f.write("\n")
                         p=int(entryList[i][3])+1
                         perc=(p*100)/30
                         f.writelines(f'{name},{tStr},{dStr},{p},{30},{perc}')
                 
                i+=1
attendance("ASHISH_PATIL")
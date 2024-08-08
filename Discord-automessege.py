import requests 
import datetime
import time

#URLS of discord chats you want to send messeges
Target= ""
Target1 ="" 
Target2 = ""

#Your Discord token -- Dont share this its Hash of your discord password :3
headers = {
    "Authorization" : ""
}

print("   ")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")   
print("HHH    HHH   EEEEEEEE   LLLL      LLLL      OOOOOOO      FFFFFF   RRRRRR      III  EEEEEEE  N   N   DDDDDDD    SSSSSS")
print("HHH    HHH   EEEE       LLLL      LLLL     OOO   OOO     FFF      RRR   RRR   III  EEE      N   N   DDD   DDD  SSS   ")
print("HHHHHHHHHH   EEEEEEEE   LLLL      LLLL     OOO   OOO     FFFFFF   RRRRRR      III  EEEEEEE  NN  N   DDD    DD  SSSSSS")
print("HHH    HHH   EEEE       LLLL      LLLL     OOO   OOO     FFF      RRR  RRR    III  EEE      N M N   DDD   DDD       S")
print("HHH    HHH   EEEEEEEE   LLLLLLL   LLLLLLL   OOOOOOO      FFF      RRR   RRR   III  EEEEEEE  N  MN   DDDDDDD    SSSSSS")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("                                                                                                                     ")
print("1. Number 1 = morning                                                                                                ")
print("2. Number 2 = afternoon         5.If you want to start use -1                                                        ")
print("3. Number 3 = night                                                                                                  ")
print("   ")

DayTime = int((input("Part of day ? "))) 
 

match DayTime:
 case 1:
  print(" ")
  print("Morning")
  print(" ")
  file = open("Clocks-Morning.txt","w")
  MorningHour = int(input("Enter Hours:"))
  file.write("Hours: \n") and file.write(str(MorningHour)) and file.write("\n")
  MorningMinut = int(input("Enter Minutes:"))
  file.write("Minutes: \n") and file.write (str(MorningMinut))and file.write("\n")
  MorningContext = str(input("Enter Text "))
  file.write("Context: \n") and file.write (str(MorningContext))and file.write("\n")
  print("-------------") 
  file.close
  DayTime = int((input("Part of day ? "))) 
  

match DayTime:
 case 2:
  print(" ")
  print("Afternoon")
  print(" ")
  file = open("Clocks-Afternoon.txt","w")
  file.readline
  
  AfterHour = int(input("Enter Hours:")) 
  file.write("Hours: \n") and file.write(str(AfterHour)) and file.write("\n")
  AfterMinut = int(input("Enter Minutes:"))
  file.write("Minutes: \n") and file.write (str(AfterMinut))and file.write("\n")
  AfterContext = str(input("Enter Text "))
  file.write("Context: \n") and file.write (str(AfterContext))and file.write("\n")
  print("-------------")
  DayTime = int((input("Part of day ? "))) 

  file.close()

match DayTime:
 case 3:
  print(" ")
  print("Night")
  print(" ")
  file = open("Clocks-Night.txt","w")
  NightHour = int(input("Enter Hours:")) 
  file.write("Hours: \n") and file.write(str(NightHour)) and file.write("\n")
  NigtMinut = int(input("Enter Minutes:"))
  file.write("Minutes: \n") and file.write (str(NigtMinut))and file.write("\n")
  NightContext = str(input("Enter Text "))
  file.write("Context: \n") and file.write (str(NightContext))and file.write("\n")
  print("-------------")
  DayTime = int((input("Part of day ? "))) 



SendSec = int(1)


if(DayTime == -1 ):
   print(" ")
   print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
   print("SSSSS  TTTTTT    A      RRRR    TTTTTT  ")
   print("SS       TT     A A     R  RR     TT    ")
   print("SSSS     TT    AAAAA    RRRR      TT    ")
   print("   SS    TT   A     A   R  RR     TT    ")
   print("SSSS     TT   A     A   R   RR    TT    ")
   print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
   print(" ")
   file = open("Clocks-Morning.txt","r")
   lines = file.readlines()
   MorningHourText =lines[1].strip() 
   MorningMinutText =lines[3].strip() 
   MorningContextText = lines[5].strip()
   SendSec = int(1)
   MorningHour = int(str(MorningHourText))
   MorningMinut = int(str(MorningMinutText)) 
   MorningContext = str(str(MorningContextText))

   print("Morning")
   print("Morning Hours: " + MorningHourText + ":"+ MorningMinutText)

   print("Your text: " + MorningContextText)
   print(" ")
   print("Afternoon")
   file = open("Clocks-Afternoon.txt","r")
   lines = file.readlines()
   AfterHourText =lines[1].strip() 
   AfterMinutText =lines[3].strip() 
   AfterContextText = lines[5].strip()
   AfterHour = int(str(AfterHourText))
   AfterMinut = int(str(AfterMinutText)) 
   AfterContext = str(str(AfterContextText))
   print("Afternoon Hours: " + AfterHourText + ":" + AfterMinutText)
   print("Your text: " + AfterContextText)

   print(" ")
   print("Night")
   file = open("Clocks-Night.txt","r")
   lines = file.readlines()
   NightHourText =lines[1].strip() 
   NightMinutText =lines[3].strip() 
   NightContextText = lines[5].strip()
   NightHour = int(str(NightHourText))
   NightMinut = int(str(NightMinutText)) 
   NightContext = str(str(NightContextText))
   print("Night Hours: " + NightHourText+":"+ NightMinutText)
  
   print("Your text: " + NightContextText)
   print(" ")
  


#if USA_OR_NORMAL == "am":
# MorningHour-=12
 
dayload = {
"content" : MorningContext
}

afternoon = {
"content" : AfterContext
}

nightload = {
    "content" : NightContext
}


while True:
   if MorningHour== datetime.datetime.now().hour and MorningMinut == datetime.datetime.now().minute and SendSec == datetime.datetime.now().second:
    requests.post(Target, dayload, headers = headers) and requests.post(Target1, dayload, headers = headers) and requests.post(Target2, dayload, headers = headers)
    time.sleep(1)  
    
   if NightHour== datetime.datetime.now().hour and NightMinut == datetime.datetime.now().minute and SendSec == datetime.datetime.now().second:
      requests.post(Target, nightload, headers = headers) and requests.post(Target1, nightload, headers = headers) and requests.post(Target2, nightload, headers = headers)
      time.sleep(1)  
   if AfterHour== datetime.datetime.now().hour and AfterMinut == datetime.datetime.now().minute and SendSec == datetime.datetime.now().second:
      requests.post(Target, afternoon, headers = headers) and requests.post(Target1, afternoon, headers = headers) and requests.post(Target2, afternoon, headers = headers)
      time.sleep(1)  



 
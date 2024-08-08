from sys import stderr
import requests
from datetime import datetime
import time

# URLS of discord chats you want to send messeges
target_set=["","",""]

# Your Discord token -- Dont share this its Hash of your discord password :3
headers = {
    "Authorization": ""
}

print("")
print(" -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print(" HHH    HHH   EEEEEEEE   LLLL      LLLL      OOOOOOO      FFFFFF   RRRRRR      III  EEEEEEE  N   N   DDDDDDD    SSSSSS")
print(" HHH    HHH   EEEE       LLLL      LLLL     OOO   OOO     FFF      RRR   RRR   III  EEE      N   N   DDD   DDD  SSS   ")
print(" HHHHHHHHHH   EEEEEEEE   LLLL      LLLL     OOO   OOO     FFFFFF   RRRRRR      III  EEEEEEE  NN  N   DDD    DD  SSSSSS")
print(" HHH    HHH   EEEE       LLLL      LLLL     OOO   OOO     FFF      RRR  RRR    III  EEE      N M N   DDD   DDD       S")
print(" HHH    HHH   EEEEEEEE   LLLLLLL   LLLLLLL   OOOOOOO      FFF      RRR   RRR   III  EEEEEEE  N  MN   DDDDDDD    SSSSSS")
print(" -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("                                                                                                                      ")
print("1. If you want to start use number 4                                                                                  ")
print("2. Number 2 = afternoon                                                                                               ")
print("3. Number 1 = morning                                                                                                 ")
print("4. Number 3 = night                                                                                                   ")


def get_info(day_part):
    print(f"{day_part}\n")
    with open(f"Clocks-{day_part}.txt", "w") as file:
        hour = int(input("Enter Hours:"))
        file.write(f"Hours: \n{hour}\n")
        minut = int(input("Enter Minutes:"))
        file.write(f"Minutes: \n{minut}\n")
        context = str(input("Enter Text "))
        file.write(f"Context: \n{context}\n")
        print("-------------")
    return hour, minut, context

while True:
    try:
        DayTime = int((input("Part of day ? ")))
    except ValueError:
        print("Please enter a number", file=stderr)
        continue
    options = {1:"Morning",2:"Afternoon",3:"Night"}
    if DayTime in options.keys():
        hour, minut, context = get_info(options[DayTime])
    elif DayTime == 4:
        break
    else :
        print("Please enter a number between 1 and 3", file=stderr)
        continue


def load_file(day_part):
    try:
        with open(f"Clocks-{day_part}.txt", "r") as file:
            lines = file.readlines()
            hour = int(lines[1].strip())
            minut = int(lines[3].strip())
            context = lines[5].strip()

        print(f"{day_part} Hours: {hour} {minut}")
        print(f"Your text: {context}\n")
        return hour, minut, context
    except FileNotFoundError:
        print(f"File {day_part} not found", file=stderr)
        return None


print(" ")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("SSSSS  TTTTTT    A      RRRR    TTTTTT  ")
print("SS       TT     A A     R  RR     TT    ")
print("SSSS     TT    AAAAA    RRRR      TT    ")
print("   SS    TT   A     A   R  RR     TT    ")
print("SSSS     TT   A     A   R   RR    TT    ")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

"""remind_dict = {
    "Morning":load_file("Morning"),
    "Afternoon":load_file("Afternoon"),
    "Night":load_file("Night")
}"""

remind_dict = {}
for key in {"Morning", "Afternoon", "Night"}:
    value = load_file(key)
    if value is not None:
        remind_dict.update({key: value})

"""remind_dict = {
    key:load_file(key)
    for key in {"Morning","Afternoon","Night"}
    if load_file(key) is not None
}"""

print(remind_dict)

# if USA_OR_NORMAL == "am":
# MorningHour-=12


while True:
    for hour,minut,context in remind_dict.values():
        dayload = {"content": context}
        now = datetime.now()
        for target in target_set:
            if hour == now.hour and minut == now.minute and 1 == now.second:
                print(target)
                result = requests.post(target, dayload, headers=headers)
                print(result)
                time.sleep(1)
    time.sleep(0.5)
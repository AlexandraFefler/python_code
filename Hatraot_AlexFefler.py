from enum import Enum
import math

area = "" # area
seconds = 0 # number of seconds according to threat
ifMeyaretet = "" #text if kipat barzel attacks or not
d = 0 # d = distance
class Threats(Enum):
    PATZMAR = 1
    ROCKET = 2
    BALON_TAVURA = 3
    FALSE_ALARM = 4
class Areas(Enum):
    ALEF = 1
    BET = 2
    GIMEL = 3
    OPEN = 4

t = int(input("Enter threat type: ")) # t = threat
x = int(input("Enter x: "))
y = int(input("Enter y: "))

if (t==1): #if threat 1
    seconds = "30 seconds"
    if ((x>=0 and x<=20 and y>0 and y<=20) or (x>0 and x<=20 and y>=0 and y<=20)):
        if (x>10 and x<=20 and y>10 and y<=20): #if area alef + external boundaries
            area = str(Areas(1)).removeprefix("Areas.")
            area = "Area: " + area
            d = math.sqrt(math.pow(x,2)+math.pow(y,2)) # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        elif (x>10 and x<=20 and y>=0 and y<10): #if area bet + external boundaries
            area = str(Areas(2)).removeprefix("Areas.")
            area = "Area: " + area
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))  # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        elif (x>=0 and x<10 and y>10 and y<=20): #if area gimel + external boundaries
            area = str(Areas(3)).removeprefix("Areas.")
            area = "Area: " + area
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))  # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        elif (x>0 and x<10 and y>0 and y<10): #if area 4 - open area + external boundaries
            seconds = ""
            area = str(Areas(4)).removeprefix("Areas.")
            area = "Area: "+area
            ifMeyaretet = "" #kipat barzel doesn't attack when the threat is going to fall in an open area
        elif (x==10 and y>=0 and y<10): #gvul bein open le bet
            # about open and bet
            area = "Area: BET and OPEN"
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))  # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        elif (y==10 and x>10 and x<=20): #gvul bein bet le alef
            # about bet and alef
            area = "Area: BET and ALEF"
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))  # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        elif (x==10 and y>10 and y<=20): #gvul bein alef le gimel
            # about alef and gimel
            area = "Area: ALEF and GIMEL"
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))  # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        elif (y==10 and x>=0 and x<10): #gvul bein gimel le open
            # about gimel and open
            area = "Area: GIMEL and OPEN"
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))  # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        elif (x==10 and y==10): #center
            # message about alef, bet, gimel and open
            area = "Area: ALEF, BET, GIMEL and OPEN"
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))  # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        print(str(area) + "\n" + str(seconds) + "\n" + str(ifMeyaretet))
    else:
        print("Please, enter valid x and y values")
elif (t==2): #if threat 2
    seconds = "60 seconds"
    if ((x>=0 and x<=20 and y>0 and y<=20) or (x>0 and x<=20 and y>=0 and y<=20)):
        if (x>10 and x<=20 and y>10 and y<=20): #if area alef + external boundaries
            area = str(Areas(1)).removeprefix("Areas.")
            area = "Area: " + area
            d = math.sqrt(math.pow(x,2)+math.pow(y,2)) # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        elif (x>10 and x<=20 and y>=0 and y<10): #if area bet + external boundaries
            area = str(Areas(2)).removeprefix("Areas.")
            area = "Area: " + area
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))  # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        elif (x>=0 and x<10 and y>10 and y<=20): #if area gimel + external boundaries
            area = str(Areas(3)).removeprefix("Areas.")
            area = "Area: " + area
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))  # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        elif (x>0 and x<10 and y>0 and y<10): #if area 4 - open area + external boundaries
            seconds = ""
            area = str(Areas(4)).removeprefix("Areas.")
            area = "Area: "+area
            ifMeyaretet = "" #kipat barzel doesn't attack when the threat is going to fall in an open area
        elif (x==10 and y>=0 and y<10): #gvul bein open le bet
            # about open and bet
            area = "Area: BET and OPEN"
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))  # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        elif (y==10 and x>10 and x<=20): #gvul bein bet le alef
            # about bet and alef
            area = "Area: BET and ALEF"
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))  # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        elif (x==10 and y>10 and y<=20): #gvul bein alef le gimel
            # about alef and gimel
            area = "Area: ALEF and GIMEL"
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))  # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        elif (y==10 and x>=0 and x<10): #gvul bein gimel le open
            # about gimel and open
            area = "Area: GIMEL and OPEN"
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))  # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        elif (x==10 and y==10): #center
            # message about alef, bet, gimel and open
            area = "Area: ALEF, BET, GIMEL and OPEN"
            d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))  # distance check
            if (d < 13):
                ifMeyaretet = "Kipat Barzel attacks"
            else:
                ifMeyaretet = "Kipat Barzel does not attack"
        print(str(area) + "\n" + str(seconds) + "\n" + str(ifMeyaretet))
    else:
        print("Please, enter valid x and y values")
elif (t==3): #if threat 3
    seconds = "120 seconds"
    if ((x>=0 and x<=20 and y>0 and y<=20) or (x>0 and x<=20 and y>=0 and y<=20)):
        if (x>10 and x<=20 and y>10 and y<=20): #if area alef + external boundaries
            area = str(Areas(1)).removeprefix("Areas.")
            area = "Area: " + area
            ifMeyaretet = "Kipat Barzel does not attack"
        elif (x>10 and x<=20 and y>=0 and y<10): #if area bet + external boundaries
            area = str(Areas(2)).removeprefix("Areas.")
            area = "Area: " + area
            ifMeyaretet = "Kipat Barzel does not attack"
        elif (x>=0 and x<10 and y>10 and y<=20): #if area gimel + external boundaries
            area = str(Areas(3)).removeprefix("Areas.")
            area = "Area: " + area
            ifMeyaretet = "Kipat Barzel does not attack"
        elif (x>0 and x<10 and y>0 and y<10): #if area 4 - open area + external boundaries
            seconds = ""
            area = str(Areas(4)).removeprefix("Areas.")
            area = "Area: "+area
            ifMeyaretet = "" #kipat barzel doesn't attack when the threat is going to fall in an open area
        elif (x==10 and y>=0 and y<10): #gvul bein open le bet
            # about open and bet
            area = "Area: BET and OPEN"
            ifMeyaretet = "Kipat Barzel does not attack"
        elif (y==10 and x>10 and x<=20): #gvul bein bet le alef
            # about bet and alef
            area = "Area: BET and ALEF"
            ifMeyaretet = "Kipat Barzel does not attack"
        elif (x==10 and y>10 and y<=20): #gvul bein alef le gimel
            # about alef and gimel
            area = "Area: ALEF and GIMEL"
            ifMeyaretet = "Kipat Barzel does not attack"
        elif (y==10 and x>=0 and x<10): #gvul bein gimel le open
            # about gimel and open
            area = "Area: GIMEL and OPEN"
            ifMeyaretet = "Kipat Barzel does not attack"
        elif (x==10 and y==10): #center
            # message about alef, bet, gimel and open
            area = "Area: ALEF, BET, GIMEL and OPEN"
            ifMeyaretet = "Kipat Barzel does not attack"
        print(str(area) + "\n" + str(seconds) + "\n" + str(ifMeyaretet))
    else:
        print("Please, enter valid x and y values")
elif (t==4): #if threat 4
    print("False alarm!")
else:
    print("Please, enter a valid threat number")


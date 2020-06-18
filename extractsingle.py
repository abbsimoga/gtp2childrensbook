import os

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

fw = open('CBTest.txt', "a")

for direction in os.listdir("C:/Users/User/Documents/GitHub/gtp2childrensbook/data"):
    print(direction)
    fr = open("data/"+direction, "r")
    for line in fr:
        charremoveamount = 0

        while RepresentsInt(line[charremoveamount]) or line[charremoveamount] == " ":
            charremoveamount+=1
        
        fw.write(line[charremoveamount:])
    fr.close()
fw.close()
# HAD TO DELETE FILES TO COMMIT CUZ 2 LARGE OF FILES
# HERES THE DATASET: http://www.thespermwhale.com/jaseweston/babi/CBTest.tgz

# go through each file in data and write each row to cbtest.txt withouth each int in beggining of line

# check if line[0] has int if so remove or copy the rest:

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


#DONT OPEN CBTest IT WILL CRASH LAMAO


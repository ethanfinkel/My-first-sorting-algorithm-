table = [2,1,7,8,4,5,1,2,8,2,10,78,5678,626,27,3,8, 12,16,7,4,50,12,213,424,544,2456254,25622,111,1,2,3,4,22,1,3]
x=0
start=0
checkB = False
switch =0
i=0

def check (list=[], *args):
    right =0
    x = 0
    while x < len(list):
        if list[x] < list[x+1]:
            right = right +1
            x +=1
        else:
            return False
            break
        if right == len(list):
            return True
            break

while i < 1000000:
    while checkB is False:
        print (x)
        if table[x] < table[x+1]:
            x +=1
            print ("pass")
        elif table[x] == table [x+1]:
            x = x+1
        else:
            print(table[x],table [x+1])
            switch =table[x+1]
            table[x+1] = table[x]
            table [x] = switch
            x =0
            print(table)
            print ("switch")
            break
    i = i+1
    if check (table) == True:
        print "sorted"
        break

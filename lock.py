from itertools import permutations
import sys
import re
'''
function to find combinations for each clues
'''
def findcombinations(number, R, W):

    p= permutations(number)

    newlist= []


    for j in numbers:
        if int(j)<10 :
            j = '00'+j
        elif int(j)>=10 and int(j)<100:
            j= '0' +j
        strvalue = j[0] + j[1] + j[2]


        if R == '0' and W == '0':
            # if j[0]!=number[0] and j[1]!=number[1] and j[2]!=number[2]:
            #     count =0
            #     for c in number:
            #         if c in strvalue:
            #             count +=1
            #     if count==0 and (number[0] not in j and number[1] not in j and number[2] not in j):
                    #if j[0] not in number and j[1]not in number and j[2]not in number:
            if(number[0] not in j and number[1] not in j and number[2] not in j):
                        newlist.append(strvalue)
        elif R=='0'and W =='1':
            if j[0]!=number[0] and j[1]!=number[1] and j[2]!=number[2] :
                # for c in number:
                #     if c in  strvalue :
                #         newlist.append(strvalue)
                #         break
                count=0
                for c in number:
                    if c in strvalue:
                        count +=1
                if count == 1 :
                #if (number[0]  in j or number[1]  in j or number[2]  in j):
                    newlist.append(strvalue)
        elif R=='0'and W =='2':
            count= 0

            if j[0]!=number[0] and j[1]!=number[1] and j[2]!=number[2] :
                for c in number:
                    if c in strvalue:
                        count +=1
                if count == 2 :
                    newlist.append(strvalue)
        elif R=='0'and W =='3':
            count= 0
            if j[0]!=number[0] and j[1]!=number[1] and j[2]!=number[2] :
                for c in number:
                    if c in strvalue:
                        count +=1
                if count == 3 :
                    newlist.append(strvalue)
        elif R == '1' and W == '0':
            if (j[0]==number[0] and j[1]!=number[1] and j[2]!=number[2] and (number[1] not in j and number[2] not in j))  :#or (j[0]!=number[0] and j[1]==number[1] and j[2]!=number[2])or (j[0]!=number[0] and j[1]!=number[1] and j[2]==number[2]):
                newlist.append(strvalue)
            elif (j[0]!=number[0] and j[1]==number[1] and j[2]!=number[2] and (number[0] not in j and number[2] not in j))  :
                newlist.append(strvalue)
            elif (j[0]!=number[0] and j[1]!=number[1] and j[2]==number[2] and (number[0] not in j and number[1] not in j))  :
                newlist.append(strvalue)
        elif R == '2' and W == '0':
            if (j[0]==number[0] and j[1]==number[1] and j[2]!=number[2]) or (j[0]!=number[0] and j[1]==number[1] and j[2]==number[2])or (j[0]==number[0] and j[1]!=number[1] and j[2]==number[2]):
                newlist.append(strvalue)
        elif R == '1' and W == '1':
            if (j[0] == number[0] and j[1] != number[1] and j[2] != number[2]) or (
                    j[0] != number[0] and j[1] == number[1] and j[2] != number[2]) or (
                    j[0] != number[0] and j[1] != number[1] and j[2] == number[2]):
                # for c in number:
                #     if c in strvalue:
                #         newlist.append(strvalue)
                #         break
                count = 0
                for c in number:
                    if c in strvalue:
                        count += 1
                if count == 2:
                    newlist.append(strvalue)
    # for R and W both >0 only permutation of input number are required
    for j in p:
        strvalue= j[0]+j[1]+j[2]
        if R == '1' and W=='2':
            if j[0]==number[0] and j[1]!=number[1] and j[2]!=number[2]:
                newlist.append(strvalue)
            if j[1]==number[1] and j[0]!=number[0] and j[2]!=number[2]:
                newlist.append(strvalue)
            if j[2] == number[2] and j[0] != number[0] and j[1] != number[1]:
                newlist.append(strvalue)


        elif R == '2' and W =='1':
            if j[0]==number[0] and j[1]==number[1] and j[2]!=number[2]:
                newlist.append(strvalue)
            if j[0]==number[0] and j[2]==number[2] and j[1]!=number[1]:
                newlist.append(strvalue)
            if j[1] == number[1] and j[2] == number[2] and j[0] != number[0]:
                newlist.append(strvalue)


    return newlist

## function body ends



##parse arguments
if len(sys.argv)<2:
    print("ERROR: Must provide at least one pattern of the form XYZ-R-W")
    sys.exit()
inputlist = sys.argv[1:]
numbers = [str(x) for x in range(000,1000) ]
list = []



print("Trying : ",str(inputlist))
for element in inputlist:
    number=element[:3]
    R=element[4:5]
    W=element[6:]

    if(re.search('\d{3}-\d-\d',element)== None):    #regex check for valid input
        print("ERROR: invalid argument: ",element)
        sys.exit()
    elif(int(R)+int(W)>3):
        print("R + W should be <=3 , Try again")
        sys.exit()
    elif( R=='3'):
        out=number
        print("****Solution #1 ",number)
        sys.exit()
    else:
        out=findcombinations(number, R, W)
    list.append(set(out))

# find intersection of all possible combination's of all the clues
u =set.intersection(*list)
if len(u)==0:
    print("No solutions found.")
else :

    for id, val in enumerate(u):
        print(f'**** Solution  #{id+1} is {val}')

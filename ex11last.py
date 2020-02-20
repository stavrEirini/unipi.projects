from ex11list import *
###creating two new lists from the list of the file###
newlist=list[0]
newlist2=list[1]
print(newlist)
print(newlist2)
from collections import Counter 
givelist=[]
for i in range(6):
    give_number= input("please give a number that your list contains:" )
    givelist.append(give_number)#creating a list of the numbers given
print(givelist)
find=0
f=0
###checking if there is a list available###
counter=Counter(givelist)#getting how many times every item appears in each list
counter2=Counter(newlist)
counter3=Counter(newlist2)
for i in range(6):
    for j in range(4):
        if (givelist[i]== newlist[j]):#if items are equal
            if (counter[givelist[i]]==counter2[newlist[j]]):#and if the times they appear in both lists are the same count
             find=find+1
if(find==4):#if count=4 there is an available list(a list that contains the same items appearing the same times
    print("a list exists")
else:
    find=0 #if count is not for check the other list
    for i in range(6):
        for j in range(4):
            if(givelist[i]== newlist2[j]):
                if(counter[givelist[i]]==counter3[newlist2[j]]):
                    f=f+1

if(f==4):
    print("a list exists")
else:
     f=0
if(find==0 and f==0):#if none=4 there is no available list
    print("there is no list containing the given numbers available")
                    

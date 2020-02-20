
#dictionary of items in stock
avitems = {
    "apple": 2,
    "cheese": 3,
    "eggs": 2.5,
    "juice": 4,
    "chocolate": 1.5
    }

def addlist(item):
    itemsList=[]
    ###while the user continues giving items loop###
    while (item !=""):
        if item in avitems: #if the item is available put it on the list#
            print("item available")
            itemsList.append(item)
            item=input("please enter your shopping item: ")
        else:
                print("no item available please give another")
                item=input("please enter your shopping item: ")
        if (item ==""):
            return itemsList;

def findcost(l,cost):
    c=0
    for product in l:
        value= avitems[product]
        cost= cost+value
        c= c+1
        if (c== len(l)): #if in final loop return the sum of prices
            return cost;
        
        
item = input("please enter your shopping item: ")
l= addlist(item) #call the function that adds items to list
print(l)
cost=0
total= findcost(l,cost) #call the function that adds the list's itemsinput
print(total)
tax= total*24/100
totalcost= tax+total
print("your shopping cost is:",totalcost,"euros")

    
    
    

    

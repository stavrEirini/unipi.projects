#function to find sum of the number's digits
def findsum(number):
    #add the digits and return the sum
    s=0
    ###if the number given is negative turn it to positive###
    if (number<0):
        number= number*-1
        while (number>0):
                digits= number % 10
                s= s + digits
                number= number//10
                ###return the sum only if all digits are added###
                if (number<=0): #return the negative sum
                    return s*(-1);
    else:
            number=number
            while (number>0):
                digits= number % 10
                s= s + digits
                number= number//10
                ###return the sum only if all digits are added###
                if (number<=0):
                    return s;

    
number= int(input("please enter number: "))
while (number >9 or number< -9):
    number=number*3+1
    number= findsum(number)
    print(number)
    
    
        
        
        
    

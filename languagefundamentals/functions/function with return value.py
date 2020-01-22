#function to add two numbers taking 2 arguments and assign the return value to another variable
# def add(no1,no2):
#     res=no1+no2
#     return res
# val=add(10,20)
# print(val)
def reverse():
    while(num!=0):
        digit=num%10 #last digit extract
        reverse=((reverse*10)+digit)
        num=num//10 #the num value changes ,so do the loop condition
    print("result",reverse)
    return reverse
reverse()
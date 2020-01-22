# while(condition)
#     body of the loop
# i=0
# while(i<10):
#     print(i)
#     i+=1
#reverse
# i=10
# while(i>0):
#     print(i)
#     i-=1

# # factorial
# num=int(input("enter value"))
# i=1
# res=1
# while(i<=num):
#     res=res*i
#     i+=1
# print(res,"result")

# reverse a number
def reverse():
num=int(input("enter a 3 digit number"))#321
reverse=0
while(num!=0):
    digit=num%10 #last digit extract
    reverse=((reverse*10)+digit)
    num=num//10 #the num value changes ,so do the loop condition
print("result",reverse)








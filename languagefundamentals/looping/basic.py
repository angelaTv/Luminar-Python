print(" Question 1")
# print numbers from 0 to 9
for i in range(0,10):
    print(i)

print(" Question 2")
# print numbers from 0 to 9 in reverse
for i in range(10,0,-1):
    print(i)

print(" Question 3")
# print numbers from 0 to 9 even numbers
lw=int(input("enter lower limit"))
up=int(input("enter lower limit"))
for i in range(lw,up):
    if(i%2==0):
      print(i)
    else:
      print("odd")

print(" Question 4")
# print numbers square of even numbers from given range
# lw=int(input("enter lower limit"))
# up=int(input("enter lower limit"))
# for i in range(lw,up):
#     if(i%2==0):
#       print(i*i)
#     else:
#       print("odd")
print(" Question 5")
#  check prime number or not of a given number(prime number has only 1 and the number itself as factors

# no=int(input("enter a number"))
# for i in range(2,no):                         #accept number till that inputed value
#     if (no%i==0):                             #if not prime ie factors are there
#         flg=1   #flg=flg+1                           #till the loop continue the flag increments
#         break
#     else:
#         flg=0
#                                     #is prime,Ie only 1 and the number itself
#
# if (flg==0):
#     print(no,"is prime a number")
# else:
#     print("not a prime")

# to check prime or not in given range
lw=int(input("enter a number"))
up=int(input("enter a number"))
for j in range(lw,up):
    for i in range(2,j):                         #accept number till that inputed value
        if (j%i==0):                             #if not prime ie factors are there
            flg=1   #flg=flg+1                           #till the loop continue the flag increments
            break
        else:
            flg=0
                                        #is prime,Ie only 1 and the number itself

    if (flg==0):
        print(j,"is prime a number")
    else:
        print(j,"not a prime")
        print("Question" )
      # predict the out put
      #   for i in range (1.11):
      #       if(i==5):
      #           break
      #       print(i)
    print("Question")
        # predict the out put

        # for i in range (1.11):
        #     if(i==5):
        #         continue #skips 5
        #     print(i)

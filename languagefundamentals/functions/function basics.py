#cube of a number
# def cub():
#    n= int(input("enter number"))
#    res=n**3
#    print(res)
# cub()
#is even or not
# def isevenodd():
#
#     if(n%2!=0):
#         print("even")
#     else:
#         print("odd")
# isevenodd(21)
#fibonocii series up to nth term
def fibonocii():
    n1=0
    n2=1
    count=0
    terms=int(input("how many terms"))
    while (count<terms):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
fibonocii()





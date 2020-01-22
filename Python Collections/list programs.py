# to find even numbers in a given list
numb = []
eve = []
n = int(input("enter the range"))
for j in range(0, n):
    val = int(input("enter the number"))
    numb.append(val)
# num[i]=val
# print (numb)
cnt = len(numb)
# print(cnt)
for i in numb:
    if i % 2 == 0:
        # print(i)
        eve.append(i)
    else:
        pass
print(eve)

# to find even numbers in a given list do square and sum of it
numb = []
eve = []
n = int(input("enter the range"))
for j in range(0, n):
    val = int(input("enter the number"))
    numb.append(val)
# num[i]=val
print(numb, "is the entered list")
cnt = len(numb)
# print(cnt)
for i in numb:
    if i % 2 == 0:
        # print(i)
        eve.append(i)
    else:
        pass
sumo = 0
sq = []
print(eve, "are the even numbers")
for item in eve:
    va = item * item
    sq.append(va)
    # print(va,"is the square of",item)
    sumo += va
print(sq, "are the squares of all even numbers")
print(sumo, "is the sum of squares of all even numbers")
# Or by list comprehension
n = int(input("enter the range"))
numb = [j for j in range(0, n)]
print(numb, "is the entered list")
cnt = len(numb)
eve = [i for i in numb if i % 2 == 0]
print(eve, "are the even numbers")
sq = [item * item for item in eve]
print(sq, "are the squares of even numbers")
sumo = 0
for item in sq:
    sumo += item
print(sumo, "is the sum of squares of all even numbers")

# to search a element inside a list(linear search)
numb = []
n = int(input("enter the range"))
for j in range(0, n):
    val = int(input("enter the number"))
    numb.append(val)
print(numb, "is the entered list")

fin = int(input("Enter the element you want to find"))
cnt = 0
for i in numb:
    if i == fin:
        cnt += 1
        # print("element found at position",i)
        break
    else:
        cnt = 0
if cnt == 0:
    print("element is not there in the list")
else:
    print("element found")

# binary search
numb = []  # to get values from user
n = int(input("enter the range"))
for j in range(0, n):
    val = int(input("enter the number"))
    numb.append(val)
print(numb, "is the entered list")
numb.sort()
print(numb, "is the sorted list")
lo = 0
up = len(numb)
mid = (up + lo) // 2
element = int(input("Enter the element you want to find"))
flg = 0
while lo < up:
    if element > numb[mid]:
        low = mid + 1
        print("new lower=", lo)
    elif element < numb[mid]:
        up = mid - 1
        print("new upper=", up)
    elif element == numb[mid]:
        flg += 1
        break
    mid = (lo + up) // 2
    if lo > up:
        break

    print("new mid", mid)

if flg == 0:
    print("element not found ")
else:
    print("element found at position", mid)

# Python3 implementation of simple method
# to find count of pairs with given sum.

# Returns number of pairs in arr[0..n-1]
# with sum equal to 'sum'

numb = [1, 5, 6, 0, 7, -1]
n = len(numb)
sumo = int(input("enter the sum "))
cnt = 0
for i in range(0, n):
    for j in range(i + 1, n):
        if numb[i] + numb[j] == sumo:
            cnt += 1
            print(numb[i], ",", numb[j], end="\n ")
print("There are ", cnt, " pairs")
#OR
def getpa(numb,sumo):
    n = len(numb)
    cnt = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if numb[i] + numb[j] == sumo:
                cnt += 1
                print(numb[i], ",", numb[j], end="\n ")
    print("There are ", cnt, " pairs")


# num = [1, 5, 6, 0, 7, -1]
num = []  # to get values from user
n = int(input("enter the range"))
for j in range(0, n):
    val = int(input("enter the number"))
    num.append(val)
print(num, "is the entered list")
sumot = int(input("enter the sum "))
getpa(num, sumot)

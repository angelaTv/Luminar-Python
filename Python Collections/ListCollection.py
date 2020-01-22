marks=[50,"welcome","true",50.1]
print(marks)
#list
marks=[10,10,20,30.5,"math"]#can add duplicates
print(marks)
marks[0]=15
print(marks)#mutable
#insersion order is preserved
#to add a value in last
marks.append(13)
print(marks)
#to insert in specific location
marks.insert(0,18)
print(marks)
#to iterate through list
cnt=len(marks)
print(cnt)
for i in range(0,cnt):
    print(marks[i])

# # 000
# # 111
# # 222
# for i in range(0,3):
#     for j in range(0,3):
#         print(i,end="")
#     print()

# # *
# # * *
# # * * *
#
# for i in range(0,3):
#     for j in range(0,i+1):
#         print("*",end="")
#     print()

# # 1
# # 12
# # 123
# for i in range(0,3):
#     for j in range(0,i+2):
#         print(j,end="")
#     print()

# # 123
# # 12
# # 1
# for i in range(3,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# 4444
# 333
# 22
# 1
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()

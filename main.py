print("Before change")
list = [1,2,3]
# print(list[0])

for i in list:
    print(i)

print("After change")
list[0] = 7

for i in list:
    print(i)
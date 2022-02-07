# import array as arr


var = "purushottam kumar"
print(var)
print(var[0])
print(var[3:9])
print(var[-4])
print((var * 2))

a = 577
b = 99
c = 7

if (a > b) and (a > c):
    print("a is greatest number:", a)
elif (b > c):
    print("b is greatest number:", b)
else:
    print("c is greatest number:", c)

# p = arr.array('i',[1,2,30,4,5,6,7,8,9,22,33,15])
arr = [1, 33, 2, 1, 45, 78]

for i in range(0, 5):
    print(arr[i])
    # print("\r")

arr.append(0)
print(arr)
arr.insert(4, 100)
print(arr)
arr.pop(4)
print(arr)

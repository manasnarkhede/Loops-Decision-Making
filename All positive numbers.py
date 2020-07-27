#Python program to print positive numbers

list1 = [11, -21, 0, 45, 66, -93]
print(list1)

for num in list1:
    if num >= 0:
        print(num, end = " ")

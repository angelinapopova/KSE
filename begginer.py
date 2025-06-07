#1
a = [1,6,23]
total = sum(a)
print(total)

#2
a = [13,6,23]
a_min = min(a)
print(a_min)

#3
a = [13,6,23]
a_reversed = a[::-1]
print(a_reversed)

#4
a = [13,6,23]
for i in a:
    if i % 2 != 0:
        print(i)

#5
a = [13,6,23]
num = int(input("Enter a number:"))
result = [x * num for x in a]
print(result)
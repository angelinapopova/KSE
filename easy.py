#1
nums = [3,7,43,13,36]
n = int(input("Enter a number:"))
for i in nums:
    if i > n:
        print(i)

#2
from statistics import mean
nums = [3,7,43,13,36]
nums_mean = mean(nums)
print(nums_mean)

#3
nums = [3,7,43,13,36]
n = int(input("Enter a number:"))
filtered = [i for i in nums if i < n]
count = len(filtered)
print("Numbers less then {n}:", filtered)
print("Quantity of such numbers:" , count)

#4
nums = [3,7,43,13,36]
n = int(input("Enter a number:"))
num = [i for i in nums if i % n == 0]
result = sum(num)
print(result)

#5
nums = [3,7,43,13,36]
nums_squared = [i**2 for i in nums]
print(nums_squared)
    
#6
nums = [-3,7,-43,13,36]
positive = []
for i in nums:
    if i > 0:
        positive.append(i)
print(positive)

#7
words = ["money", "monkey", "machine", "mile", "month" ]
prefix = "mo"
result = [word for word in words if word.lower().startswith(prefix.lower())]
print(result)

#8
nums = [-3,7,-43,13,36]
n = int(input("Enter a number:"))
num_sum = sum(nums[:n])
print(num_sum)

#9
words = ["level", "phone", "madam", "water"]
palindrom =[]
for word in words:
    if word == word[::-1]:
        palindrom.append(word)
print(palindrom)

#10
nums = [-3,7,-43,13,36]
n = int(input("Enter a devider:"))
new_nums = [ i % n == 0 for i in nums]
print(new_nums)
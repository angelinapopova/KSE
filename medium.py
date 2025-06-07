#1
nums = [3,7,43,13,36]
x = int(input("Enter a number:"))
y = int(input("Enter a number:"))
num = [i for i in nums if i % x == 0 and i % y != 0]
print(num)

#2
import itertools
full_names = [["Angelina", "Popova"], ["Daria", "Volovyk"]]
full_names_new = list(itertools.chain.from_iterable(full_names))
print(full_names_new)

#3
text = "kYiviSThEcaPItaLofUKRaiNe"
caps = [letter for letter in text if letter.isupper()]
print(caps)

#4
from collections import Counter
nums = [3,7,43,13,36,7,14,3,6,36,7]
nums.sort(reverse=True)
counter = Counter(nums)
def frequency(x):
    return -counter[x]
sorted_nums = sorted(nums, key=frequency)
print(nums)
print(sorted_nums)

#5
import itertools
full_names = [["Angelina", "Popova"], ["Daria", "Volovyk"]]
full_names_new = list(itertools.chain.from_iterable(full_names))
full_names_new_2 = []
for ithem in full_names_new:
    if "o" in ithem:
        full_names_new_2.append(ithem)
print(full_names_new_2)

#6
from collections import Counter
grades = {
    ("student1", 10),
    ("student2", 11),
    ("student2", 9),
    ("student1", 12),
    ("student1", 10)
}
total = Counter()
for key, value in grades:
    total[key]+=value
print(total)

#7
from collections import Counter
nums = [3,7,43,13,36,7,14,3,6,36,7]
counts = Counter(nums)
new_nums = [0 if counts[x] >= 2 else x for x in nums]
print(new_nums)

#8
words = ["apple", "yes", "dictionary", "month", "python"]
x = int(input("Enter a number:"))
words_new = [i for i in words if len(i) > x]
lenght = len(words_new)
print(lenght)

#9
import itertools
students = ["Anna:","Lily:","Harry:","Zayn:"]
grades = [8,9,12,10]
progress = []
for i in range(len(students)):
    progress.append(students[i])
    progress.append(grades[i])
print(progress)

#10
nums = [3,7,43,13,36]
x = int(input("Enter a number:"))
y = int(input("Enter a number:"))
result = []
for i in nums:
    if i > x:
        result.append(i*y)
print(result)

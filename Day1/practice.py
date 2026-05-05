#Print even numbers from 1 to 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
#Find maximum in a list
numbers = [10, 45, 23, 67, 12]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("Max:", max_num)
#Count frequency of elements
nums = [1,2,2,3,3,3,4]
freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)
#Function to calculate sum of list
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total
print(sum_list([1,2,3,4]))
#Reverse a string
text = "harshitha"
print(text[::-1])
#second largest number in a list
nums = [10, 20, 4, 45, 99]
first=secomd=float("-inf")
for i in nums:
    if i>first:
        second=first
        first=i
    elif i>second and i<first:
       second=i
print("Second largest:", second)
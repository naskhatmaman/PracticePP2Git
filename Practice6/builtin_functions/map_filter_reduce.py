from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

#1 Use map to square numbers
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

#2 Use filter to get even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even:", even)

#3 Use reduce to calculate sum
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)

#4 Use sum, min, max
print("Sum:", sum(numbers))
print("Min:", min(numbers))
print("Max:", max(numbers))

#5 Use sorted with reverse
print("Sorted desc:", sorted(numbers, reverse=True))

#6 Combine map + filter
result = list(map(lambda x: x*10, filter(lambda x: x > 3, numbers)))
print("Filtered & mapped:", result)
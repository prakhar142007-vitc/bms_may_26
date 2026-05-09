def insertion_sort(numbers,n):
    for i in range(n):
        element = numbers[i]
        j = i - 1
        while j >= 0 and element < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = element
    print(numbers)
'''n=int(input("Enter number of elements:"))
numbers = []
for i in range(n):
    ele = int(input())
    numbers.append(ele)
a = insertion_sort(numbers , n)
print(a)'''